import socket
import multiprocessing

import client_handler

TCP_IP = "127.0.0.1"
TCP_PORT = 5005
BUFFER_SIZE = 1024


class Server:
	def __init__(self, ip, port):
		self.ip = ip
		self.port = port
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		
		self.manager = multiprocessing.Manager()

		# Keys are user IDs
		self.bike_pipes = self.manager.dict()
		
		self.active_connections = dict()
		
	def start(self):
		self.socket.bind((self.ip, self.port))
		self.socket.listen(1)
		
		self.wait_for_clients()
		
	def wait_for_clients(self):
		while True:
			conn, addr = self.socket.accept()
			
			print "Accepted a client, forking..."
			new_handler = client_handler.Client_Handler(conn, addr, self.bike_pipes)
			
			new_handler.start()
			
			self.active_connections[addr] = new_handler
			
		self.cleanup()
		
	def cleanup(self):
		for addr, p in self.active_connections:
			p.join()
		
		self.socket.close()
		
def fork_client_handler(conn, addr, bike_pipes):
	print "\tIn client handler process..."
	handler = client_handler.Client_Handler(conn, addr, bike_pipes)
	
	print "\tCreated client handler"
	
	handler.start()

if __name__ == "__main__":
	server = Server(TCP_IP, TCP_PORT)
	server.start()
	