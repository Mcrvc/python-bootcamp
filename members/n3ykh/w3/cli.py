"""Command-line study planner."""

import argparse
from datetime import date
from pathlib import Path

from members.n3ykh.w2.io_utils import load_tasks


def parse_date(value: str) -> date:
    """Parse a date in YYYY-MM-DD format."""
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("date must use YYYY-MM-DD format") from exc


def parse_hours(value: str) -> float:
    """Parse a positive number of available study hours."""
    try:
        hours = float(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("hours must be a number") from exc

    if not 0 < hours < float("inf"):
        raise argparse.ArgumentTypeError("hours must be finite and greater than 0")

    return hours


def main() -> int:
    """Load tasks and print a study plan within the available time."""
    parser = argparse.ArgumentParser(description="Create a study plan")
    parser.add_argument("csv_file", type=Path, help="path to the tasks CSV")
    parser.add_argument(
        "--hours",
        type=parse_hours,
        required=True,
        help="available study time in hours",
    )
    parser.add_argument(
        "--today",
        type=parse_date,
        default=date.today(),
        help="planning date in YYYY-MM-DD format (default: today)",
    )
    args = parser.parse_args()

    try:
        tasks = load_tasks(args.csv_file)
    except FileNotFoundError:
        parser.exit(1, f"error: file not found: {args.csv_file}\n")
    except (ValueError, OSError) as exc:
        parser.exit(1, f"error: cannot load tasks: {exc}\n")

    # Earliest deadlines first; use importance to break deadline ties.
    tasks.sort(key=lambda task: (task.deadline, -task.importance, task.title))

    remaining = args.hours
    print(f"Tonight ({args.hours:.1f} h):")

    item_number = 0
    for task in tasks:
        if remaining <= 0:
            break

        if task.deadline < args.today or task.effort_h <= 0:
            continue

        allocated = min(task.effort_h, remaining)
        item_number += 1
        print(f"  {item_number}. {task.title} ...... {allocated:.1f} h")
        remaining -= allocated

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
