#!/usr/bin/env python3

class Time:
    def __init__(self, hour=0, minute=0, second=0):
        if not (isinstance(hour, int) and isinstance(minute, int) and isinstance(second, int)):
            raise TypeError("All arguments must be integers")
        self.hour = hour
        self.minute = minute
        self.second = second

def sum_times(t1, td):
    # Convert both time objects to seconds
    seconds1 = time_to_sec(t1)
    seconds2 = time_to_sec(td)
    
    # Sum the seconds
    total_seconds = seconds1 + seconds2
    
    # Convert the total seconds back to a Time object
    return sec_to_time(total_seconds)

    return Time(new_hour, new_minute, new_second)

def format_time(t):
    return f"{t.hour:02}:{t.minute:02}:{t.second:02}"

def change_time(time, seconds):
    # Convert the time object to seconds
    total_seconds = time_to_sec(time)
    
    # Add the specified seconds to the total
    total_seconds += seconds
    
    # Ensure the hour wrapping around a 24-hour clock by taking modulo of total_seconds with 86400 (number of seconds in 24 hours)
    total_seconds %= 86400

    # Convert the new total seconds back to a Time object
    new_time = sec_to_time(total_seconds)
    
    # Update the original time object
    time.hour = new_time.hour
    time.minute = new_time.minute
    time.second = new_time.second

    return None


def valid_time(time):
    if not (0 <= time.second < 60 and 0 <= time.minute < 60 and 0 <= time.hour < 24):
        return False
    return True

...
...
def time_to_sec(time):
    '''convert a time object to a single integer representing the number of seconds from mid-night'''
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def sec_to_time(seconds):   
    '''convert a given number of seconds to a time object in hour,minute,second format'''
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes,60)
    return time
...
...

