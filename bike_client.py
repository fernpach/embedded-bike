"""
bike_client
"""
# Uncomment when ready to test on board
#import mraa
import random
import socket
from collections import OrderedDict

SERVER_IP = "127.0.0.1"
SERVER_PORT = "5005"

USER = 0xbad

WORKOUT_ID = -1


METRIC_KEYS = ['workout_id', 'speed', 'distance',
               'calories_burned', 'heart_rate', 'timestamp']


def sample(workout_id):
    raw_data = []
    raw_data.append(workout_id)
    raw_data += _sample()
    raw_data.append(datetime.now())

    return OrderedDict(zip(METRIC_KEYS, raw_data))


def _sample():
    # This will read GPIO pins (eventually)
    # for testing let's just make something up
    speed = random.randint(1, 20)
    distance = random.randint(1, 10)
    calories_burned = random.randint(1, 300)
    heart_rate = random.randint(1, 120)

    return [speed, distance,
            calories_burned, heart_rate]


def connect():
	global(USER)
	global(SERVER_IP)
	global(SERVER_PORT)
	global(WORKOUT_ID)
	
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((SERVER_IP, SERVER_PORT))
	
	initial_msg = {"user": USER, "client_type": 0}
	
	s.send(initial_msg)
	
	server_ack = s.recv(1024)
	
	
	if not server_ack["user"] == USER:
		print "Error: User mismatch in server ack"
		s.close()
		
	WORKOUT_ID = server_ack["workout_id"]


def main():
    pass


if __name__ == '__main__':
    main()
