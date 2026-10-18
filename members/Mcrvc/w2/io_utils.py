import csv
import json
from datetime import datetime
from pathlib import Path

from members.Mcrvc.w2.models import Task


def load_tasks(path: str | Path) -> list[Task]:
    tasks = []
    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for line_num, row in enumerate(reader, start=2):
            try:
                tasks.append(Task(
                    title=row["title"].strip(),
                    importance=int(row["importance"]),
                    effort_h=float(row["effort_h"]),
                    deadline=datetime.strptime(row["deadline"].strip(), "%Y-%m-%d").date(),
                ))
            except (ValueError, KeyError) as e:
                raise ValueError(f"line {line_num}: bad row ({e})")
    return tasks


def save_json(tasks: list[Task], path: str | Path) -> None:
    data = []
    for t in tasks:
        data.append({
            "title": t.title,
            "importance": t.importance,
            "effort_h": t.effort_h,
            "deadline": t.deadline.isoformat(),
        })
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
