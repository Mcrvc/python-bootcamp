import csv
import json
from datetime import date

from .models import Task

def load_tasks(path: str) -> list[Task]:
    tasks: list[Task] = []

    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            line_no = reader.line_num
            try:
                task = Task(
                    title=row["title"],
                    importance=int(row["importance"]),
                    effort_h=float(row["effort_h"]),
                    deadline=date.fromisoformat(row["deadline"]),
                )
            except KeyError as e:
                raise ValueError(
                    f"line {line_no}: missing column {e}"
                ) from e
            except ValueError as e:
                raise ValueError(
                    f"line {line_no}: {e}"
                ) from e

            tasks.append(task)

    return tasks


def save_json(tasks: list[Task], path: str) -> None:
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
        json.dump(data, f, indent=2, ensure_ascii=False)