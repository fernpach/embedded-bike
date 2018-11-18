"""
bike_client
"""
import time
#import mraa
import random
from collections import OrderedDict


SECONDS_PER_SAMPLE = 1

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
    pass


def main():
    # connect to server
    session_id = 0

    # Sample GPIO pins for workout
    # data
    while True:
        workout_data = sample(session_id)
        time.sleep(SECONDS_PER_SAMPLE)



if __name__ == '__main__':
    main()
