import csv
from datetime import date
import json

try:
    from .models import Task
except ImportError:
    from models import Task


def load_tasks(path) -> list[Task]:
    tasks = []
    with open(path, mode="r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        header = next(reader, None)  

        for row in reader:
            line_no = reader.line_num
            if not row or len(row) != 4:
                raise ValueError(f"Line {line_no}: Expected 4 columns, got {len(row) if row else 0}")

            try:
                title = row[0].strip()
                importance = int(row[1])
                effort_h = float(row[2])
                deadline = date.fromisoformat(row[3].strip())

                task = Task(title=title, importance=importance, effort_h=effort_h, deadline=deadline)
            except Exception as e:
                raise ValueError(f"Line {line_no}: {e}") from e

            tasks.append(task)

    return tasks


def save_json(tasks: list[Task], path) -> None:
    data = [
        {
            "title": t.title,
            "importance": t.importance,
            "effort_h": t.effort_h,
            "deadline": t.deadline.isoformat(),
        }
        for t in tasks
    ]
    with open(path, mode="w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)