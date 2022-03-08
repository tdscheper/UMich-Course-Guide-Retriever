"""Utility functions."""
from typing import Optional


# Time format: "8:00 AM", "12:30 PM"


def time_hour_min(time: str) -> Optional[str]:
    time = time.split()
    return time[0] if len(time) == 2 else None

def time_period(time: str) -> Optional[str]:
    time = time.split()
    return time[1] if len(time) == 2 else None

def time_hour(time: str) -> Optional[int]:
    time = time_hour_min(time)
    if time is None:
        return None
    time = time.split(':')
    hour = time[0] if len(time) == 2 else None
    if hour is None or not hour.isdigit() or not 1 <= int(hour) <= 12:
        return None
    return int(hour)

def time_min(time: str) -> Optional[int]:
    time = time_hour_min(time)
    if time is None:
        return None
    time = time.split(':')
    min = time[1] if len(time) == 2 else None
    if min is None or not min.isdigit() or not 0 <= int(min) <= 59:
        return None
    return int(min)

def escape_time(time: str) -> str:
    escaped = ''
    for char in time:
        escaped += char if char != ' ' else '%20'
    return escaped

def valid_time(time: str) -> bool:
    return (
        time_hour(time) is not None
        and time_min(time) is not None
        and time_period(time) is not None
    )

def time_less(lhs: str, rhs: str) -> bool:
    lhr, lmin = time_hour(lhs), time_min(lhs)
    rhr, rmin = time_hour(rhs), time_min(rhs)
    if lhr != rhr:
        return lhr < rhr
    return lmin < rmin
