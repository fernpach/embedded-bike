"""
bike_client
"""
# Uncomment when ready to test on board
#import mraa
import random
from datetime import datetime


METRIC_KEYS = ['workout_id', 'speed', 'distance',
               'calories_burned', 'heart_rate', 'timestamp']


def sample():
    raw_data = _sample()

    return dict(zip(METRIC_KEYS, raw_data))


def _sample():
    # This will read GPIO pins (eventually)
    # for testing let's just manufacture data
    wid = generate_workout_id()       # unique workout id 
    speed = random.randint(1, 20)     # miles/hr
    distance = random.randint(1, 10)  # miles
    calories_burned = random.randint(1, 300)
    heart_rate = random.randint(1, 120)
    timestamp = datetime.now()

    return [wid, speed, distance, calories_burned,
            heart_rate, timestamp]


def generate_workout_id():
    
