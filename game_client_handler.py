import struct
import client_handler
import json

BUFFER_SIZE = 1024

OPCODE_NOP				= 0
OPCODE_START_GAME		= 1
OPCODE_STOP_GAME		= 2


class Game_Client_Handler():
	def __init__(self, parent_handler, pipe_out):
		self.user = user
		self.parent_handler = parent_handler
		self.on_no_data = self.nop
		self.pipe_out = pipe_out
		
		ack_message = {"user": self.parent_handler.user}
		
		self.parent_handler.send_to_client(ack_message)
		
		
	def handle_message(self, data):
		try:
			opcode = data["opcode"]
		
		except:
			self.parent_handler.fatal_error("Missing attributes in message from game client")
		
		if opcode == OPCODE_NOP:
		
			return
			
		elif opcode == OPCODE_START_GAME:
		
			self.on_no_data = self.pass_along_bike_samples
			return
			
		elif opcode == OPCODE_STOP_GAME:
		
			self.on_no_data = self.nop
			return
			
	def attempt_to_start_game(self):
		if self.user in self.parent_handler.bike_connections:
			self.on_no_data = self.pass_along_bike_samples
		
		else:
			# notify game client that no bike client was found
			err_msg = {"error" : "no bike client"}
			
			self.parent_handler.send_to_client(json.dumps(err_msg))
		
	def pass_along_bike_samples(self):
		# pop samples from queue and send to client
		while self.pipe_out.poll():
			try:
				new_sample = self.pipe_out.recv()
				self.parent_handler.send_to_client(new_data)
				
			except EOFError:
				# notify client that other bike client disconnected
				break
			
	def nop(self):
		return
		
	def cleanup(self):
		self.pipe_out.close()