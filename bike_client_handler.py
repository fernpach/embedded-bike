import struct
import client_handler

class Bike_Client_Handler():
	def __init__(self, parent_handler):
		self.parent_handler = parent_handler
		
		
	def handle_message(self, data):
		try:
			workout_id = data["workout_id"]
			speed = data["speed"]
			distance = data["distance"]
			calories_burned = data["calories_burned"]
			heart_rate = data["heart_rate"]
			time_stamp = data["time_stamp"]
			
		except KeyError:
			self.parent_handler.fatal_error("Missing attributes in sample from bike")