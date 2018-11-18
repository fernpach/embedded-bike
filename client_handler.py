import socket
import json

import multiprocessing
import traceback

import game_client_handler
import bike_client_handler


BUFFER_SIZE = 1024

BIKE_CLIENT_TYPE = 0
GAME_CLIENT_TYPE = 1



class Client_Handler(multiprocessing.Process):
	def __init__(self, conn, addr, bike_pipes):
		multiprocessing.Process.__init__(self, target=self.begin_handling, args=())
		
		self.conn = conn
		self.addr = addr
		self.bike_pipes = bike_pipes
		
		self.client_type = -1
		
		self.user = -1
		
		self.handler = None
		
	def begin_handling(self):
	
		# receive initial message with user ID and client type
		data = self.conn.recv(BUFFER_SIZE)
		if not data:
			
			self.fatal_error("connection closed before information about client could be parsed")
			
		else:
			print "\tReceived valid data"
			
			data_dict = json.loads(data.decode('utf-8'))
			
			print "\tDecoded json"
			
			try:
				self.client_type = data_dict['client_type']
				self.user = data_dict['user']
				
			except KeyError:
				self.fatal_error("user and/or client_type not found in initial message")
				
				
			
			if self.client_type == BIKE_CLIENT_TYPE:
				# check to see if the pipe has already been created
				# if so, grab the pipe in and use it
				# otherwise, create it
				if self.user in self.bike_pipes:
					pipe_in = self.bike_pipes[self.user][0]
				else:
					pipe_in, pipe_out = multiprocessing.Pipe()
					#self.bike_pipes[self.user] = (None, pipe_out)
					self.bike_pipes[self.user] = (None, None)
				
				self.handler = bike_client_handler.Bike_Client_Handler(self, pipe_in)
				
			elif self.client_type == GAME_CLIENT_TYPE:
				# check to see if the pipe has already been created
				# if so, grab the pipe out and use it
				# otherwise, create it
				if self.user in self.bike_pipes:
					pipe_out = self.bike_pipes[self.user][1]
				else:
					pipe_in, pipe_out = multiprocessing.Pipe()
					self.bike_pipes[self.user] = (pipe_in, None)
					
				
				self.handler = game_client_handler.Game_Client_Handler(self, pipe_out)
				
			else:
				self.fatal_error("Unknown client type")
		
		# begin waiting for messages from clients
		self.conn.settimeout(0.001)
		
		while True:
			try:
				data = self.conn.recv(BUFFER_SIZE)
				
				if not data:
					self.print_message("Connection closed")
					break
					
				else:
					data_dict = json.loads(data.decode('utf-8'))
					self.client.handle_message(data_dict)
					
			except socket.timeout:
				self.handler.on_no_data()
				self.clear_bike_sample_queue()
				
			except EOFError:
				break
				
		self.cleanup()
		
	def send_to_client(self, message):
		self.conn.send(message)
		
	def fatal_error(self, message):
		print "Client_Handler {}: FATAL ERROR: {}\nExiting...".format(self.addr, message)
		
		self.cleanup()
		exit()
		
	def print_message(self, message):
		print "Client_Handler {}: {}".format(self.addr, message)
		
	def clear_bike_sample_queue(self):
		"""
		Clear pipe to prevent samples piling up when no one is listening
		"""
		if self.user in self.bike_pipes:
			pipe_out = self.bike_pipes[self.user][1]
			
			if not pipe_out == None:
				# pop and discard samples
				while pipe_out.poll():
					try:
						_ = pipe_out.recv()
						
					except EOFError:
						# notify client that other bike client disconnected
						break
			else:
				# pipe_out has a listener, no need to clear pipe
				return
		
	def cleanup(self):
		self.handler.cleanup()
		self.conn.close()

		# TO-DO: remove pipes from pipe dict when both are closed
		if self.client_type == BIKE_CLIENT_TYPE:
			pass
			
		elif self.client_type == GAME_CLIENT_TYPE:
			pass
		
		



