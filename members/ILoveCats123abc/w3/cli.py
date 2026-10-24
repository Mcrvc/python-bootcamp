"""Command-line interface for the study planner."""

import argparse
import sys
from datetime import date, datetime
from pathlib import Path

from members.ILoveCats123abc.w2.io_utils import load_tasks


def main():
    """Run the study planner CLI tool to parse tasks, allocate study hours, and display the plan."""
    parser = argparse.ArgumentParser(
        description="Study planner CLI tool from CSV tasks."
    )

    parser.add_argument(
        "csv_path", type=str, help="Path to the tasks CSV file"
    )
    parser.add_argument(
        "--hours",
        type=float,
        required=True,
        help="Available study hours today",
    )
    parser.add_argument(
        "--today",
        type=str,
        default=None,
        help="Target date in YYYY-MM-DD format (Default: today)",
    )

    args = parser.parse_args()

    if args.today:
        try:
            today_date = datetime.strptime(args.today, "%Y-%m-%d").date()
        except ValueError:
            print(
                f"Error: Date '{args.today}' is invalid. Use YYYY-MM-DD format.",
                file=sys.stderr,
            )
            sys.exit(1)
    else:
        today_date = date.today()

    csv_file = Path(args.csv_path)
    if not csv_file.exists():
        print(f"Error: File '{args.csv_path}' does not exist!", file=sys.stderr)
        sys.exit(1)

    try:
        tasks = load_tasks(str(csv_file))
    except (FileNotFoundError, ValueError) as e:
        print(f"Error reading CSV file: {e}", file=sys.stderr)
        sys.exit(1)

    valid_tasks = [t for t in tasks if t.deadline >= today_date]
    valid_tasks.sort(key=lambda t: (t.deadline, -t.importance))

    allocated_hours = 0.0
    plan = []

    for task in valid_tasks:
        if allocated_hours >= args.hours:
            break
        remaining_hours = args.hours - allocated_hours
        time_spent = min(task.effort_h, remaining_hours)
        allocated_hours += time_spent
        plan.append((task.title, time_spent))

    print(f"Tonight ({allocated_hours:.1f} h):")
    for i, (title, time_spent) in enumerate(plan, 1):
        print(f"{i}. {title:<20} {time_spent:.1f} h")

if __name__ == "__main__":
    main()