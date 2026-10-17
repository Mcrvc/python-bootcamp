"""Entry point for running: python -m members.n3ykh.w2"""
from __future__ import annotations

import sys
from pathlib import Path

from .io_utils import load_tasks

# Từ members/n3ykh/w2/__main__.py đi ngược lên 3 cấp thư mục sẽ về thư mục gốc python-bootcamp/
ROOT_DIR = Path(__file__).resolve().parents[3]
DEFAULT_CSV = ROOT_DIR / "samples" / "tasks.csv"


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    csv_path = Path(args[0]) if args else DEFAULT_CSV

    tasks = load_tasks(csv_path)
    for task in tasks:
        print(
            f"{task.title} (importance={task.importance}, "
            f"effort={task.effort_h}h, deadline={task.deadline})"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())