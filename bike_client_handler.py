import struct
import client_handler
import hashlib

import time

class Bike_Client_Handler():
	def __init__(self, parent_handler, pipe_in):
		self.parent_handler = parent_handler
		self.pipe_in = pipe_in
		
		# generate a workout id, send back to client
		
		h = hashlib.md5()
		h.update(time.time())
		h.update(parent_handler.user_id)
		
		self.workout_id = h.hexdigest()
		
		ack_message = {"user": self.parent_handler.user, "workout_id" = self.workout_id}
		
		self.parent_handler.send_to_client(ack_message)
		
		
	def handle_message(self, data):
		# check for message integrity before passing it along
		try:
			workout_id = data["workout_id"]
			speed = data["speed"]
			distance = data["distance"]
			calories_burned = data["calories_burned"]
			heart_rate = data["heart_rate"]
			time_stamp = data["time_stamp"]
			
		except KeyError:
			self.parent_handler.fatal_error("Missing attributes in sample from bike")
			
		if workout_id != self.workout_id:
			self.parent_handler.fatal_error("Workout ID mismatch in message from bike")
			
		
		self.pipe_in.send(data)
		
	def on_no_data(self):
		return
		
	def cleanup(self):
		self.pipe_in.close()