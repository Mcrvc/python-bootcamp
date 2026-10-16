from pathlib import Path

from .io_utils import load_tasks

SAMPLE = Path(__file__).resolve().parents[3] / "samples" / "tasks.csv"


def main() -> None:
    for task in load_tasks(SAMPLE):
        print(f"{task.title} (importance {task.importance}) requires {task.effort_h} hours and is due on {task.deadline}.")


if __name__ == "__main__":
    main()