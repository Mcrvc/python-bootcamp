"""W3-3: command-line study planner.

Usage (run from the python-bootcamp folder):
    python -m members.tbanh2516_dot.w3.cli samples/tasks.csv \
        --hours 2 --today 2026-10-26

Output:
    Tonight (2.0 h):
      1. Assignment ...... 1.5 h
      2. DS exam ......... 0.5 h
"""

import argparse
import sys
from datetime import date
from pathlib import Path

from ..w2.io_utils import load_tasks
from ..w2.models import Task


def allocate(tasks: list[Task], hours: float, today: date) -> list[tuple[Task, float]]:
    """Share the available hours between tasks, most urgent first (greedy).

    Priority of a task = importance / days_left, with days_left of at least 1
    so a task due today does not cause a division by zero.

    Args:
        tasks: Tasks loaded from the CSV file.
        hours: Hours available tonight.
        today: Reference date used to compute days_left.

    Returns:
        (task, hours_given) pairs in priority order; tasks that get 0 hours
        are left out.
    """
    ordered = sorted(
        tasks, key=lambda t: t.importance / max(t.days_left(today), 1), reverse=True
    )
    remaining = hours
    result: list[tuple[Task, float]] = []
    for task in ordered:
        give = min(task.effort_h, remaining)
        if give <= 0:
            break
        result.append((task, give))
        remaining -= give
    return result


def render(plan: list[tuple[Task, float]], hours: float) -> str:
    """Format the plan like the example in section 18.7 of the tutorial.

    Args:
        plan: (task, hours_given) pairs from allocate().
        hours: Total hours available, shown in the header.

    Returns:
        The text to print.
    """
    lines = [f"Tonight ({hours:.1f} h):"]
    for i, (task, given) in enumerate(plan, start=1):
        lines.append(f"  {i}. {(task.title + ' ').ljust(17, '.')} {given:.1f} h")
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    """Create the argument parser for the planner CLI."""
    parser = argparse.ArgumentParser(description="Plan tonight's study session.")
    parser.add_argument(
        "csv", type=Path, help="CSV file with title,importance,effort_h,deadline"
    )
    parser.add_argument(
        "--hours", type=float, required=True, help="hours available tonight"
    )
    parser.add_argument(
        "--today",
        type=date.fromisoformat,
        default=date.today(),
        help="reference date YYYY-MM-DD (default: today), for reproducible results",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """Run the CLI and return the process exit code (0 = ok, 1 = error).

    Args:
        argv: Command-line arguments; None means use sys.argv.
    """
    args = build_parser().parse_args(argv)
    try:
        tasks = load_tasks(args.csv)
    except FileNotFoundError:
        print(f"error: file not found: {args.csv}", file=sys.stderr)
        return 1
    except ValueError:
        print(f"error: invalid CSV: {args.csv}", file=sys.stderr)
        return 1
    plan = allocate(tasks, args.hours, args.today)
    print(render(plan, args.hours))
    return 0


if __name__ == "__main__":
    sys.exit(main())
