"""Week 2 CLI entry point that prints the sample plan."""

from datetime import date
from pathlib import Path

from members.Mcrvc.w2.io_utils import load_tasks

ROOT = Path(__file__).resolve().parents[3]
SAMPLE = ROOT / "samples" / "tasks.csv"


def main() -> None:
    """Print the sample study plan with days-left for each task."""
    try:
        tasks = load_tasks(SAMPLE)
    except FileNotFoundError:
        print("sample file not found:", SAMPLE)
        return
    for t in tasks:
        left = t.days_left(date.today())
        print(t.title, "| importance", t.importance, "|",
              t.effort_h, "h | due", t.deadline, "|", left, "days left")


if __name__ == "__main__":
    main()
