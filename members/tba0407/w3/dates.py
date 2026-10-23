"""Utilities for parsing human-friendly due dates."""

import calendar
import re
from datetime import date, timedelta

WEEKDAYS = {
    name.lower(): number for number, name in enumerate(calendar.day_abbr)
}
WEEKDAYS.update(
    {name.lower(): number for number, name in enumerate(calendar.day_name)}
)


def parse_due(text: str, today: date) -> date:
    """Parse an ISO date, relative day, or weekday after ``today``."""
    value = text.strip()
    lowered = value.lower()

    try:
        return date.fromisoformat(value)
    except ValueError:
        pass

    if lowered == "tomorrow":
        return today + timedelta(days=1)

    relative = re.fullmatch(r"in\s+(\d+)\s+days?", lowered)
    if relative:
        return today + timedelta(days=int(relative.group(1)))

    if lowered in WEEKDAYS:
        days_ahead = (WEEKDAYS[lowered] - today.weekday()) % 7 or 7
        return today + timedelta(days=days_ahead)

    raise ValueError(f"unknown due date: {text}")
