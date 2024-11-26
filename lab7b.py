#!/usr/bin/env python3

class Time:
    def __init__(self, hour=0, minute=0, second=0):
        if not (isinstance(hour, int) and isinstance(minute, int) and isinstance(second, int)):
            raise TypeError("All arguments must be integers")
        self.hour = hour
        self.minute = minute
        self.second = second

def sum_times(t1, td):
    new_hour = t1.hour + td.hour
    new_minute = t1.minute + td.minute
    new_second = t1.second + td.second

    # Carry over seconds to minutes
    if new_second >= 60:
        new_minute += new_second // 60
        new_second %= 60

    # Carry over minutes to hours
    if new_minute >= 60:
        new_hour += new_minute // 60
        new_minute %= 60

    return Time(new_hour, new_minute, new_second)

def format_time(t):
    return f"{t.hour:02}:{t.minute:02}:{t.second:02}"

def change_time(time, seconds):
    time.second += seconds
    # Adjust seconds and carry/borrow as necessary
    while time.second >= 60:
        time.second -= 60
        time.minute += 1
    while time.second < 0:
        time.second += 60
        time.minute -= 1

    # Adjust minutes and carry/borrow as necessary
    while time.minute >= 60:
        time.minute -= 60
        time.hour += 1
    while time.minute < 0:
        time.minute += 60
        time.hour -= 1

    # Consider what should happen if hours go negative; for now, we assume wrap around a 24-hour clock
    if time.hour >= 24:
        time.hour %= 24
    elif time.hour < 0:
        time.hour = 24 + (time.hour % 24)  # Correctly handle negative hour wrapping

    return None


def valid_time(time):
    if not (0 <= time.second < 60 and 0 <= time.minute < 60 and 0 <= time.hour < 24):
        return False
    return True
