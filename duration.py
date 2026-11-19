#!/usr/bin/env python3
"""Parse and format durations like 1h30m and 5400 seconds."""
import re
from datetime import date, datetime

PATTERN = re.compile(
    r"\s*(?:(?P<hours>\d+)h)?\s*(?:(?P<minutes>\d+)m)?\s*(?:(?P<seconds>\d+)s)?\s*",
    re.IGNORECASE,
)


def parse_duration(text):
    compact = text.strip().lower()
    if not compact:
        raise ValueError("duration must not be empty")
    match = PATTERN.fullmatch(compact)
    if not match or not any(match.groups()):
        raise ValueError("invalid duration")
    hours = int(match.group("hours") or 0)
    minutes = int(match.group("minutes") or 0)
    seconds = int(match.group("seconds") or 0)
    if minutes > 59 or seconds > 59:
        raise ValueError("minutes and seconds must be below 60")
    return hours * 3600 + minutes * 60 + seconds


CLOCK_PATTERN = re.compile(r"^(?P<hours>\d+):(?P<minutes>\d{2}):(?P<seconds>\d{2})$")


def parse_clock(text):
    match = CLOCK_PATTERN.fullmatch(text.strip())
    if not match:
        raise ValueError("invalid clock value")
    hours = int(match.group("hours"))
    minutes = int(match.group("minutes"))
    seconds = int(match.group("seconds"))
    if minutes >= 60 or seconds >= 60:
        raise ValueError("minutes and seconds must be below 60")
    return hours * 3600 + minutes * 60 + seconds


def sum_durations(values):
    """Sum an iterable of duration strings into total seconds."""
    items = list(values)
    if not items:
        raise ValueError("values must not be empty")
    return sum(parse_duration(item) for item in items)


def breakdown(seconds):
    if seconds < 0:
        raise ValueError("seconds must not be negative")
    hours, rest = divmod(seconds, 3600)
    minutes, secs = divmod(rest, 60)
    return {"hours": hours, "minutes": minutes, "seconds": secs}


def format_duration(seconds):
    parts = breakdown(seconds)
    pieces = []
    if parts["hours"]:
        pieces.append("%dh" % parts["hours"])
    if parts["minutes"]:
        pieces.append("%dm" % parts["minutes"])
    if parts["seconds"] or not pieces:
        pieces.append("%ds" % parts["seconds"])
    return " ".join(pieces)


def format_long(seconds):
    """Format seconds as a long readable string with unit names."""
    parts = breakdown(seconds)
    days, hours = divmod(parts["hours"], 24)
    pieces = []
    for value, unit in (
        (days, "day"),
        (hours, "hour"),
        (parts["minutes"], "minute"),
        (parts["seconds"], "second"),
    ):
        if value:
            suffix = "" if value == 1 else "s"
            pieces.append("%d %s%s" % (value, unit, suffix))
    return " ".join(pieces) if pieces else "0 seconds"


def format_clock(seconds):
    """Format seconds as HH:MM:SS."""
    parts = breakdown(seconds)
    return "%02d:%02d:%02d" % (
        parts["hours"],
        parts["minutes"],
        parts["seconds"],
    )


def remaining_until(target, now=None):
    text = target.strip()
    try:
        target_dt = datetime.fromisoformat(text)
    except ValueError:
        target_dt = datetime.combine(date.fromisoformat(text), datetime.min.time())
    now_dt = now or datetime.now()
    return max(0, int((target_dt - now_dt).total_seconds()))
