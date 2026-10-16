import argparse
import sys
from datetime import date

from .io_utils import load_tasks
from .errors import InfeasiblePlan, check_feasible


def main() -> int:
    parser = argparse.ArgumentParser(prog="python -m members.ILoveCats123abc.w2")
    parser.add_argument("csv_path", help="path to tasks CSV")
    parser.add_argument("--hours", type=float, default=None,
                        help="available hours (triggers feasibility check)")
    args = parser.parse_args()

    try:
        tasks = load_tasks(args.csv_path)
    except FileNotFoundError:
        print(f"Error: file not found: {args.csv_path}", file=sys.stderr)
        return 1
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    if args.hours is not None:
        try:
            check_feasible(tasks, args.hours)
        except InfeasiblePlan as e:
            print(f"Warning: {e}", file=sys.stderr)
            return 1

    today = date.today()
    print(f"Loaded {len(tasks)} task(s):")
    for t in sorted(tasks, key=lambda x: (x.deadline, -x.importance)):
        print(f"  - {t.title} (imp={t.importance}, {t.effort_h}h, "
              f"{t.days_left(today)}d left)")
    return 0


if __name__ == "__main__":
    sys.exit(main())