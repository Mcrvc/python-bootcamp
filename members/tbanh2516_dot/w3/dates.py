"""W3-1: parse human-friendly due dates."""

import re
from datetime import date, timedelta

_WEEKDAYS: dict[str, int] = {
    "mon": 0,
    "tue": 1,
    "wed": 2,
    "thu": 3,
    "fri": 4,
    "sat": 5,
    "sun": 6,
}


_IN_DAYS = re.compile(r"in (\d+) days?")


def parse_due(text: str, today: date) -> date:
    """Convert a due-date description into a date.

    Accepted forms (case-insensitive, surrounding spaces ignored):
        "2026-10-30"  -- ISO date
        "tomorrow"    -- today + 1 day
        "in 3 days"   -- today + N days
        "Fri"         -- next occurrence of that weekday (never today itself)

    Args:
        text: The description typed by the user.
        today: The reference date, passed in so results are reproducible.

    Returns:
        The due date.

    Raises:
        ValueError: If the text matches none of the forms above.

    Example:
        >>> parse_due("Fri", date(2026, 10, 6))
        datetime.date(2026, 10, 9)
    """
    t = text.strip().lower()
    try:
        return date.fromisoformat(t)
    except ValueError:
        pass
    if t == "tomorrow":
        return today + timedelta(days=1)
    m = _IN_DAYS.fullmatch(t)
    if m:
        try:
            n = int(m.group(1))
            return today + timedelta(days=n)
        except OverflowError as err:
            raise ValueError(f"cannot understand due date: {text!r}") from err
    if t in _WEEKDAYS:
        ahead = (_WEEKDAYS[t] - today.weekday()) % 7
        if ahead == 0:
            ahead = 7
        return today + timedelta(days=ahead)
    raise ValueError(f"cannot understand due date: {text!r}")
