from __future__ import annotations

import argparse
import sys
from datetime import date, datetime, timezone
from pathlib import Path

from members.truonghuy0411.w2.io_utils import load_tasks
from members.truonghuy0411.w2.models import Task


def prioritise(tasks: list[Task], today: date) -> list[Task]:
    return sorted(
        tasks,
        key=lambda t: (-t.importance, t.deadline),
    )


def allocate(tasks: list[Task], max_hours: float) -> list[Task]:
    allocated: list[Task] = []
    total_time = 0.0
    for task in tasks:
        if total_time + task.effort_h <= max_hours:
            allocated.append(task)
            total_time += task.effort_h
    return allocated


def render(allocated_tasks: list[Task], total_hours: float) -> str:
    lines: list[str] = [f"Tonight ({total_hours:.1f} h):"]
    for idx, task in enumerate(allocated_tasks, start=1):
        prefix = f"  {idx}. {task.title} "
        suffix = f" {task.effort_h:.1f} h"
        dots_count = max(2, 30 - len(prefix) - len(suffix))
        dots = "." * dots_count
        lines.append(f"{prefix}{dots}{suffix}")
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Study planner CLI")
    parser.add_argument("tasks_file", type=str, help="Path to tasks CSV file")
    parser.add_argument(
        "--hours",
        type=float,
        default=2.0,
        help="Available study hours",
    )
    parser.add_argument(
        "--today",
        type=str,
        default=None,
        help="Reference today date YYYY-MM-DD",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    file_path = Path(args.tasks_file)
    if not file_path.exists() or not file_path.is_file():
        sys.stderr.write(f"Error: file not found '{args.tasks_file}'\n")
        sys.exit(1)

    try:
        reference_date = (
            date.fromisoformat(args.today)
            if args.today
            else datetime.now(timezone.utc).date()
        )
        tasks = load_tasks(file_path)
        ordered_tasks = prioritise(tasks, today=reference_date)
        allocated_tasks = allocate(ordered_tasks, max_hours=args.hours)
        output = render(allocated_tasks, total_hours=args.hours)
        print(output)
    except (ValueError, OSError, KeyError) as exc:
        sys.stderr.write(f"Error processing plan: {exc}\n")
        sys.exit(1)


if __name__ == "__main__":
    main()