import csv
import json
from datetime import date
from pathlib import Path

from .models import Task


def load_tasks(path: str | Path) -> list[Task]:
    """Load tasks from a CSV file with title, importance, effort_h, deadline.

    Raises:
        ValueError: If any row has invalid data types.
    """
    tasks = []
    path = Path(path)
    with path.open(mode = "r", encoding = "utf-8") as f:
        reader = csv.DictReader(f)
        for line, row in enumerate(reader, start = 2):
            try:
                title = row["title"]
                importance = int(row["importance"])
                effort_h = float(row["effort_h"])
                deadline = date.fromisoformat(row["deadline"])

                task = Task(
                    title = title,
                    importance = importance,
                    effort_h = effort_h,
                    deadline = deadline
                )
                tasks.append(task)
            except (ValueError, KeyError, TypeError) as e:
                raise ValueError(f"Invalid row at line {line} : {e}")
    return tasks

def save_json(tasks: list[Task], path: Path) -> None:
    """Save tasks as a JSON array with ISO-format deadlines."""
    path = Path(path)
    data = []
    for task in tasks:
        data.append({
            "title": task.title,
            "importance": task.importance,
            "effort_h": task.effort_h,
            "deadline": task.deadline.isoformat()
        })
    with path.open(mode = "w", encoding = "utf-8") as f:
        json.dump(data, f, indent = 4)