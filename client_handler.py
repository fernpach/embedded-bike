import socket
import json

import game_client_handler
import bike_client_handler


BUFFER_SIZE = 1024

BIKE_CLIENT_TYPE = 0
GAME_CLIENT_TYPE = 1



class Client_Handler:
	def __init__(self, conn, addr):
		self.conn = conn
		self.addr = addr
		
		self.user = -1
		
		self.handler = None
		
	def start(self):
		data = self.conn.recv(BUFFER_SIZE)
		if not data:
			
			self.fatal_error("connection closed before information about client could be parsed")
			
		else:
			data_dict = json.loads(data.decode('utf-8'))
			
			try:
				self.client_type = data_dict['client_type']
				self.user = data_dict['user']
			except KeyError:
				self.fatal_error("user and/or client_type not found in initial message")
			
			if client_type == BIKE_CLIENT_TYPE:
				self.handler = bike_client_handler.Bike_Client_Handler(self.user)
				
			elif client_type == GAME_CLIENT_TYPE:
				self.handler = game_client_handler.Game_Client_Handler(self.user)
				
			else:
				self.fatal_error("Unknown client type")
		
		
		while True:
			data = conn.recv(BUFFER_SIZE)
			
			if not data
				self.print_message("Connection closed")
				break
				
			else:
				data_dict = json.loads(data.decode('utf-8'))
				self.client.handle_message(data_dict)
				
		conn.close()
		
	def fatal_error(self, message):
		print "Client_Handler {}: FATAL ERROR: {}\nExiting...".format(self.addr, message)
		
		self.conn.close()
		exit()
		
	def print_message(self, message):
		print "Client_Handler {}: {}".format(self.addr, message)
		
		
def fork_client_handler(conn, addr):
	handler = Client_Handler(conn, addr)
	
	handler.start()