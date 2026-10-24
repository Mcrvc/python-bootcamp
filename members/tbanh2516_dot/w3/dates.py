"""W3-1 Parse human-friendly due dates."""
import re
from datetime import date, timedelta


WEEKDAYS: dict[str, int] = {"mon": 0, "tue": 1, "wed": 2, "thu": 3, "fri": 4, "sat": 5, "sun": 6}
IN_DAYS = re.compile(r"in (\d+) days?")


def parse_due(text: str, today: date) -> date:
    """Turn "2026-10-30", "tomorrow", "in 3 days" or "Fri" into a date.

    Weekday names mean the next occurrence (never today). Unknown text raises ValueError.
    """
    s = text.strip().lower()
    try:
        return date.fromisoformat(s)
    except ValueError:
        pass
    if s == "tomorrow":
        return today + timedelta(days=1)
    match = IN_DAYS.fullmatch(s)
    if match:
        try:
            return today + timedelta(days=int(match.group(1)))
        except OverflowError as err:
            raise ValueError(f"date too far in the future: {text!r}") from err

    FULL_NAMES = {"monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"}
    if s in WEEKDAYS or s in FULL_NAMES:
        key = s[:3]
        if key in WEEKDAYS:
            delta = (WEEKDAYS[key] - today.weekday()) % 7 or 7
            return today + timedelta(days=delta)

    raise ValueError(f"unknown due date: {text!r}")
