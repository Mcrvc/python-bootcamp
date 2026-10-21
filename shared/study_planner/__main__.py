"""Study planner CLI: parse CSV → prioritise → allocate → render."""

import argparse
import sys
from datetime import date

from shared.contract import Task, Block
from shared.study_planner.allocate import allocate
from shared.study_planner.parse import parse_csv
from shared.study_planner.prioritise import prioritise
from shared.study_planner.render import render


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="python -m shared.study_planner",
        description="Generate a study plan from a tasks CSV.",
    )
    parser.add_argument("csv_path", help="path to tasks CSV file")
    parser.add_argument(
        "--hours",
        type=float,
        required=True,
        help="available study hours",
    )
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
    prioritized = prioritise(tasks, today)
    blocks = allocate(prioritized, args.hours)
    print(render(blocks))
    return 0


if __name__ == "__main__":
    sys.exit(main())
