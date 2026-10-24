"""Week 3 CLI: load tasks, allocate hours, print the study plan."""

import argparse
import sys
from datetime import date

from members.Mcrvc.w2.io_utils import load_tasks
from members.Mcrvc.w2.models import Task


def allocate_hours(tasks: list[Task], hours: float) -> list[tuple[Task, float]]:
    """Greedily allocate up to hours of total study time across tasks.

    Tasks are considered in deadline-then-importance order and each task takes
    as much of the remaining budget as its effort allows.

    Args:
        tasks: The tasks to schedule.
        hours: The total available study hours.

    Returns:
        A list of (task, allocated_hours) blocks.

    """
    blocks: list[tuple[Task, float]] = []
    remaining = hours
    for task in sorted(tasks, key=lambda t: (t.deadline, -t.importance)):
        if remaining <= 0:
            break
        allocated = min(task.effort_h, remaining)
        if allocated <= 0:
            continue
        blocks.append((task, allocated))
        remaining -= allocated
    return blocks


def main() -> int:
    """Run the Week 3 CLI: load tasks, allocate hours, print the study plan.

    Returns:
        The process exit code (0 on success, 1 on error).

    """
    parser = argparse.ArgumentParser(
        prog="python -m members.Mcrvc.w3.cli",
    )
    parser.add_argument("csv_path", help="path to tasks CSV")
    parser.add_argument("--hours", type=float, default=None,
                        help="total available study hours for the plan")
    parser.add_argument("--today", type=str, default=None,
                        help="reference date YYYY-MM-DD (default: today)")
    args = parser.parse_args()

    try:
        tasks = load_tasks(args.csv_path)
    except FileNotFoundError:
        print(f"Error: file not found: {args.csv_path}", file=sys.stderr)
        return 1
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    today = date.today()
    if args.today:
        try:
            today = date.fromisoformat(args.today)
        except ValueError:
            print(f"Error: invalid --today date: {args.today}", file=sys.stderr)
            return 1

    total_hours = args.hours
    if total_hours is None:
        total_hours = sum(task.effort_h for task in tasks)
    blocks = allocate_hours(tasks, total_hours)

    for task, hours_used in blocks:
        left = (task.deadline - today).days
        left = max(left, 0)
        print(
            f"{task.title} (imp={task.importance}, {hours_used}h, "
            f"due {task.deadline}, {left}d left)",
        )

    return 0


if __name__ == "__main__":
    sys.exit(main())
