import csv
import json
from dataclasses import asdict
from datetime import date
from pathlib import Path

from .models import Task


def load_tasks(path: str | Path) -> list[Task]:
    """Load tasks from a CSV file and validate each row."""
    tasks: list[Task] = []

    with Path(path).open(encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for line_number, row in enumerate(reader, start=2):
            try:
                tasks.append(
                    Task(
                        title=row["title"],
                        importance=int(row["importance"]),
                        effort_h=float(row["effort_h"]),
                        deadline=date.fromisoformat(row["deadline"]),
                    )
                )
            except (KeyError, TypeError, ValueError) as error:
                raise ValueError(f"invalid task on line {line_number}") from error

    return tasks


def save_json(tasks: list[Task], path: str | Path) -> None:
    """Save tasks to a JSON file with ISO-formatted deadlines."""
    data: list[dict[str, object]] = []

    for task in tasks:
        item = asdict(task)
        item["deadline"] = task.deadline.isoformat()
        data.append(item)

    Path(path).write_text(json.dumps(data, indent=2), encoding="utf-8")
