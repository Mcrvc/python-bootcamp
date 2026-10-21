"""Due-date parsing for relative and ISO date strings."""


from datetime import date, timedelta
import re

_WEEKDAYS = {
    "mon": 0,
    "tue": 1,
    "wed": 2,
    "thu": 3,
    "fri": 4,
    "sat": 5,
    "sun": 6,
}


def parse_due(date_str: str, today: date) -> date:
    s = date_str.strip()

    try:
        return date.fromisoformat(s)
    except ValueError:
        pass

    low = s.lower()

    if low == "tomorrow":
        return today + timedelta(days=1)

    m = re.fullmatch(r"in\s+(\d+)\s+days?", low)
    if m:
        return today + timedelta(days=int(m.group(1)))

    if low in _WEEKDAYS:
        target_wday = _WEEKDAYS[low]
        today_wday = today.weekday()
        days_ahead = (target_wday - today_wday) % 7
        if days_ahead == 0:
            days_ahead = 7
        return today + timedelta(days=days_ahead)

    raise ValueError(f"cannot parse due date: {date_str}")
