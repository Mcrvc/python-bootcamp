from datetime import date

from shared.contract import Task


def validate(tasks: list[Task], today: date) -> list[Task]:
    """Return only valid tasks: not overdue, effort_h >= 0, importance 1-5.

    The input list is not modified. Raises TypeError if today is not a date.
    """
    if not isinstance(today, date):
        raise TypeError("today must be a datetime.date")
    return [
        t for t in tasks
        if t.deadline >= today and t.effort_h >= 0 and 1 <= t.importance <= 5
    ]
