import csv
import json
from datetime import date
from pathlib import Path

from .models import Task

def load_tasks(path: Path) -> list[Task]:
    """Read tasks from  a CSV file with header title. importance, effort_h, deadline."""
    tasks: list[Task] = []
    with open(path, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for line_no, row in enumerate(reader, start=2):  # Start at 2 to account for header
            try:
                task = Task(
                    title=row["title"],
                    importance=int(row["importance"]),
                    effort_h=float(row["effort_h"]),
                    deadline=date.fromisoformat(row["deadline"]),
                )
            except ValueError as e:
                raise ValueError(f"Error in line {line_no}: {e}") from e
            tasks.append(task)
    return tasks

def save_json(tasks: list[Task], path: Path) -> None:
    """Write tasks to a JSON file."""
    data = [
        {
            "title": t.title,
            "importance": t.importance,
            "effort_h": t.effort_h,
            "deadline": t.deadline.isoformat(),
        }
        for t in tasks
    ]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)