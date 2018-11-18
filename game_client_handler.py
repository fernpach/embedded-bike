import struct
import client_handler

BUFFER_SIZE = 1024

OPCODE_NOP				= 0
OPCODE_START_GAME		= 1
OPCODE_STOP_GAME		= 2


class Game_Client_Handler():
	def __init__(self, parent_handler):
		self.user = user
		self.parent_handler = parent_handler
		
		
	def handle_message(self, data):
		try:
			opcode = data["opcode"]
		
		except:
			self.parent_handler.fatal_error("Missing attributes in message from game client")
		
		if opcode == OPCODE_NOP:
			return
			
		elif opcode == OPCODE_START_GAME:
			return
			
		elif opcode == OPCODE_STOP_GAME:
			return