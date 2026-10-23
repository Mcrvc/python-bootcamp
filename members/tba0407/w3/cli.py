"""Command-line interface for building a small study plan."""

import argparse
import sys
from datetime import date
from pathlib import Path

from members.tba0407.w2.io_utils import load_tasks
from members.tba0407.w2.models import Task


def positive_hours(text: str) -> float:
    """Parse a non-negative number of study hours for argparse."""
    value = float(text)
    if value < 0:
        raise argparse.ArgumentTypeError("hours must be non-negative")
    return value


def build_plan(
    tasks: list[Task], available_h: float, today: date
) -> list[tuple[Task, float]]:
    """Allocate available hours to urgent tasks in priority order."""
    ordered = sorted(
        tasks,
        key=lambda task: (task.days_left(today), -task.importance),
    )
    remaining_h = available_h
    plan = []

    for task in ordered:
        if remaining_h <= 0:
            break
        hours = min(task.effort_h, remaining_h)
        if hours > 0:
            plan.append((task, hours))
            remaining_h -= hours

    return plan


def render_plan(plan: list[tuple[Task, float]]) -> str:
    """Format a study plan for terminal output."""
    total_h = sum(hours for _, hours in plan)
    lines = [f"Tonight ({total_h:.1f} h):"]

    for number, (task, hours) in enumerate(plan, start=1):
        lines.append(f"  {number}. {task.title} ...... {hours:.1f} h")

    return "\n".join(lines)


def make_parser() -> argparse.ArgumentParser:
    """Create the command-line argument parser."""
    parser = argparse.ArgumentParser(description="Build a study plan from CSV.")
    parser.add_argument("path", type=Path, help="path to a task CSV file")
    parser.add_argument("--hours", required=True, type=positive_hours)
    parser.add_argument("--today", type=date.fromisoformat, default=date.today())
    return parser


def main(argv: list[str] | None = None) -> int:
    """Run the study-planner command and return its process exit code."""
    args = make_parser().parse_args(argv)

    try:
        tasks = load_tasks(args.path)
    except (OSError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    print(render_plan(build_plan(tasks, args.hours, args.today)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
