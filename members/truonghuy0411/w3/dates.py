"""Date parsing utilities for study planner."""
from __future__ import annotations

import re
from datetime import date, timedelta

WEEKDAYS: dict[str, int] = {
    "mon": 0,
    "monday": 0,
    "tue": 1,
    "tuesday": 1,
    "wed": 2,
    "wednesday": 2,
    "thu": 3,
    "thursday": 3,
    "fri": 4,
    "friday": 4,
    "sat": 5,
    "saturday": 5,
    "sun": 6,
    "sunday": 6,
}

ISO_DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")
IN_DAYS_PATTERN = re.compile(r"^in\s+(\d+)\s+days?$", re.IGNORECASE)


def parse_due(text: str, today: date) -> date:
    """Parse human-readable due text into a concrete date object."""
    if not isinstance(text, str):
        raise TypeError("Input text must be a string")

    clean_text = text.strip()
    if not clean_text:
        raise ValueError("Due date string cannot be empty")

    lowered = clean_text.lower()

    if ISO_DATE_PATTERN.match(clean_text):
        return date.fromisoformat(clean_text)

    if lowered == "tomorrow":
        return today + timedelta(days=1)

    match_days = IN_DAYS_PATTERN.match(clean_text)
    if match_days:
        days_offset = int(match_days.group(1))
        return today + timedelta(days=days_offset)

    if lowered in WEEKDAYS:
        target_weekday = WEEKDAYS[lowered]
        days_ahead = (target_weekday - today.weekday()) % 7
        if days_ahead == 0:
            days_ahead = 7
        return today + timedelta(days=days_ahead)

    raise ValueError(f"Unknown date format: {text!r}")