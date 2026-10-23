"""Week 3 CLI: load tasks, filter by hours, print with days-left."""

import argparse
import sys
from datetime import date

from shared.study_planner.parse import parse_csv


def main() -> int:
    """Run the Week 3 CLI: load tasks, filter by hours, print with days-left.

    Returns:
        The process exit code (0 on success, 1 on error).
    """
    parser = argparse.ArgumentParser(
        prog="python -m members.Mcrvc.w3.cli"
    )
    parser.add_argument("csv_path", help="path to tasks CSV")
    parser.add_argument("--hours", type=float, default=None,
                        help="show only tasks with effort_h <= this value")
    parser.add_argument("--today", type=str, default=None,
                        help="reference date YYYY-MM-DD (default: today)")
    args = parser.parse_args()

    try:
        tasks = parse_csv(args.csv_path)
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

    if args.hours is not None:
        tasks = [t for t in tasks if t.effort_h <= args.hours]

    for t in sorted(tasks, key=lambda x: (x.deadline, -x.importance)):
        left = (t.deadline - today).days
        if left < 0:
            left = 0
        print(
            f"{t.title} (imp={t.importance}, {t.effort_h}h, "
            f"due {t.deadline}, {left}d left)"
        )

    return 0


if __name__ == "__main__":
    sys.exit(main())
