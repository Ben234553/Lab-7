#!/usr/bin/env python3
# Student ID: bsundedo

class Time:
    """Simple object type for time of the day.
       data attributes: hour, minute, second
       function attributes: __init__, __str__, __repr__, __add__,
                            time_to_sec, format_time,
                            change_time, sum_times, valid_time
    """
    def __init__(self, hour=0, minute=0, second=0):
        """Constructor for time object"""
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        """Return time object (t) as a formatted string"""
        return self.format_time()

    def __repr__(self):
        """Official string representation of Time object"""
        return f"{self.hour:02d}.{self.minute:02d}.{self.second:02d}"

    def __add__(self, t2):
        """Add two Time objects and return the sum as a new Time object."""
        total_seconds = self.time_to_sec() + t2.time_to_sec()
        return sec_to_time(total_seconds)

    def format_time(self):
        """Return time object as a formatted string"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def sum_times(self, t2):
        """Add two time objects and return the sum as a new Time object."""
        total_seconds = self.time_to_sec() + t2.time_to_sec()
        return sec_to_time(total_seconds)

    def change_time(self, seconds):
        """Change the time by a given number of seconds."""
        time_seconds = self.time_to_sec()
        nt = sec_to_time(time_seconds + seconds)
        self.hour, self.minute, self.second = nt.hour, nt.minute, nt.second
        return None

    def time_to_sec(self):
        """Convert a time object to a single integer representing the number of seconds from mid-night."""
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def valid_time(self):
        """Check for the validity of the time object attributes."""
        if not (0 <= self.hour < 24 and 0 <= self.minute < 60 and 0 <= self.second < 60):
            return False
        return True

def sec_to_time(seconds):
    '''Convert a given number of seconds to a time object in hour, minute, second format'''
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time