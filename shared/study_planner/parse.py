import csv
from datetime import datetime
from pathlib import Path
from shared.contract import Task


def parse_csv(path: str | Path) -> list[Task]:
    filepath = Path(path)
    if not filepath.exists():
        raise FileNotFoundError(f"File does not exist {filepath}")

    tasks: list[Task] = []

    with open(filepath, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        
        required_headers = {"title", "importance", "effort_h", "deadline"}
        if reader.fieldnames is None or not required_headers.issubset(set(reader.fieldnames)):
            raise ValueError("CSV file header error or column missing.")

        for line_num, row in enumerate(reader, start=2):
            try:
                title = row["title"].strip()
                importance = int(row["importance"])
                effort_h = float(row["effort_h"])
                deadline = datetime.strptime(row["deadline"].strip(), "%Y-%m-%d").date()

                task = Task(
                    title=title,
                    importance=importance,
                    effort_h=effort_h,
                    deadline=deadline
                )
                tasks.append(task)
            except (ValueError, KeyError) as e:
                raise ValueError(f"Line {line_num} data error: {e}")

    return tasks