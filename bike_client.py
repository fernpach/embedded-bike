"""
bike_client
"""
import time
#import mraa
import random
import socket
import json
from collections import OrderedDict
from datetime import datetime

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005

USER = 0xbad


SECONDS_PER_SAMPLE = 1

METRIC_KEYS = ['workout_id', 'speed', 'distance',
               'calories_burned', 'heart_rate', 'timestamp']


def sample(workout_id):
    raw_data = []
    raw_data.append(workout_id)
    raw_data += _sample()
    raw_data.append(str(datetime.now()))

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
    global USER
    global SERVER_IP
    global SERVER_PORT
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((SERVER_IP, SERVER_PORT))
    
    initial_msg = {"user": USER, "client_type": 0}
    
    s.send(json.dumps(initial_msg))
    
    server_ack = json.loads(s.recv(1024).decode('utf-8'))
    
    if not server_ack["user"] == USER:
        print "Error: User mismatch in server ack"
        s.close()
	
    return s, server_ack["workout_id"]


def main():
    # connect to server
    sock, session_id = connect()

    # Sample GPIO pins for workout
    # data
    while True:
        workout_data = sample(session_id)
        sock.send(json.dumps(workout_data))
        time.sleep(SECONDS_PER_SAMPLE)


if __name__ == '__main__':
    main()
