"""
bike_client
"""
# Uncomment when ready to test on board
#import mraa


METRIC_KEYS = ['workout_id', 'speed', 'distance',
               'calories_burned', 'heart_rate', 'timestamp']

def sample():
    raw_data = _sample()

    return dict(zip(METRIC_KEYS, raw_data))


def _sample():
    # This will read GPIO pins (eventually)
    # for testing let's just manufacture data
    
