import re
from datetime import date, timedelta

_WEEKDAYS: dict[str, int] = {
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

_IN_DAYS = re.compile(r"in (\d+) days?")


def parse_due(text: str, today: date) -> date:
    """Parse a due date from free text relative to ``today``.

    Accepts ISO dates ("2026-10-30"), "today", "tomorrow",
    "in 3 days" / "in 1 day", and weekday names ("Fri", "Friday")
    resolving to the next occurrence (never today). Unknown or
    out-of-range text raises ValueError.
    """
    cleaned = text.strip().lower()

    try:
        return date.fromisoformat(cleaned)
    except ValueError:
        pass

    if cleaned == "today":
        return today
    if cleaned == "tomorrow":
        return today + timedelta(days=1)

    match = _IN_DAYS.fullmatch(cleaned)
    if match:
        try:
            return today + timedelta(days=int(match.group(1)))
        except OverflowError as err:
            raise ValueError(f"unknown due date: {text!r}") from err

    if cleaned in _WEEKDAYS:
        delta = (_WEEKDAYS[cleaned] - today.weekday()) % 7
        if delta == 0:
            delta = 7
        try:
            return today + timedelta(days=delta)
        except OverflowError as err:
            raise ValueError(f"unknown due date: {text!r}") from err

    raise ValueError(f"unknown due date: {text!r}")
