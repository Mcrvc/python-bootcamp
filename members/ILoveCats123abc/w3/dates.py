"""Parse human-friendly due dates for the study planner."""

import re
from datetime import date, timedelta

_ISO_RE = re.compile(r"(\d{4})-(\d{2})-(\d{2})")
_IN_RE = re.compile(r"in\s+(\d+)\s+days?", re.IGNORECASE)
_WEEKDAYS = {
    "mon": 0, "monday": 0,
    "tue": 1, "tuesday": 1,
    "wed": 2, "wednesday": 2,
    "thu": 3, "thursday": 3,
    "fri": 4, "friday": 4,
    "sat": 5, "saturday": 5,
    "sun": 6, "sunday": 6,
}

def parse_due(text: str, today: date) -> date:
    """Calculate the actual date from human-readable text relative to today."""
    if not isinstance(text, str):
        raise ValueError(f"due text must be a string, got {type(text).__name__}")

    key = text.strip().lower()
    if not key:
        raise ValueError("due text is empty")

    m = _ISO_RE.fullmatch(key)
    if m:
        try:
            return date(int(m[1]), int(m[2]), int(m[3]))
        except ValueError as exc:            # e.g. 2026-02-30, month 13
            raise ValueError(f"invalid ISO date: {text!r}") from exc

    if key == "tomorrow":
        return today + timedelta(days=1)

    m = _IN_RE.fullmatch(key)
    if m:
        n = int(m[1])
        if n <= 0:
            raise ValueError(f"day count must be positive: {text!r}")
        return today + timedelta(days=n)

    if key in _WEEKDAYS:
        delta = (_WEEKDAYS[key] - today.weekday()) % 7
        return today + timedelta(days=delta or 7)

    raise ValueError(f"cannot parse due date: {text!r}")