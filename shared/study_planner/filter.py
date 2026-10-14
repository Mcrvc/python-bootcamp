from datetime import timedelta
from shared.contract import Task

def filter_upcoming(tasks, today, days) -> list[Task]:
    if days < 0:
        raise ValueError("days must be >= 0")

    horizon = today + timedelta(days=days)
    return [t for t in tasks if today <= t.deadline <= horizon]