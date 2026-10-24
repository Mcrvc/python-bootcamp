"""W3-3 Command-line study planner that reuses the W2 code."""
import argparse
import sys
from datetime import date
from pathlib import Path

from ..w2.io_utils import load_tasks
from ..w2.models import Task


def plan(tasks: list[Task], hours: float, today: date) -> list[tuple[Task, float]]:
    """Give hours to the most urgent tasks first; overdue tasks are skipped."""
    upcoming = [t for t in tasks if t.deadline >= today]
    ordered = sorted(upcoming, key=lambda t: t.importance / max(t.days_left(today), 1), reverse=True)
    result: list[tuple[Task, float]] = []
    remaining = hours
    for task in ordered:
        if remaining <= 0:
            break
        chunk = min(task.effort_h, remaining)
        result.append((task, chunk))
        remaining -= chunk
    return result


def format_plan(items: list[tuple[Task, float]]) -> str:
    """Render the plan as numbered lines with dot leaders."""
    total = sum(h for _, h in items)
    lines = [f"Tonight ({total:.1f} h):"]
    for i, (task, h) in enumerate(items, start=1):
        lines.append(f"  {i}. {(task.title + ' ').ljust(16, '.')} {h:.1f} h")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    """Parse arguments, build tonight's plan and print it. Returns the exit code."""
    parser = argparse.ArgumentParser(description="Plan tonight's study time from a task CSV.")
    parser.add_argument("file", type=Path, help="CSV with title,importance,effort_h,deadline")
    parser.add_argument("--hours", type=float, required=True, help="hours available")
    parser.add_argument("--today", type=date.fromisoformat, default=None, help="YYYY-MM-DD (default: today)")
    args = parser.parse_args(argv)

    if not args.file.exists():
        print(f"error: file not found: {args.file}", file=sys.stderr)
        return 1
    today = args.today if args.today is not None else date.today()
    print(format_plan(plan(load_tasks(args.file), args.hours, today)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
