import csv
import json
from datetime import date
from pathlib import Path

try:
    from .models import Task
except ImportError:
    from models import Task

def load_tasks(path: str | Path) -> list[Task]:
    """Read tasks from a CSV file and return a list of Task objects."""
    file_path = Path(path)
    tasks: list[Task] = []

    with file_path.open(mode="r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for line_no, row in enumerate(reader, start=2):
            try:
                if None in row.values() or not row.get("title", "").strip():
                    raise ValueError("Missing required fields or empty title")

                task = Task(
                    title=row["title"].strip(),
                    importance=int(row["importance"]),
                    effort_h=float(row["effort_h"]),
                    deadline=date.fromisoformat(row["deadline"].strip()),
                )
                tasks.append(task)
            except (ValueError, TypeError, KeyError) as exc:
                raise ValueError(f"Invalid row at line {line_no}: {exc}") from exc

    return tasks

def save_json(tasks: list[Task], path: str | Path) -> None:
    """Serialize a list of Task objects to a JSON file."""
    file_path = Path(path)
    data = [
        {
            "title": t.title,
            "importance": t.importance,
            "effort_h": t.effort_h,
            "deadline": t.deadline.isoformat(),
        }
        for t in tasks
    ]

    with file_path.open(mode="w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)