from pathlib import Path

from .io_utils import load_tasks


def main() -> None:
    sample = Path(__file__).resolve().parents[3] / "samples" / "tasks.csv"

    for task in load_tasks(sample):
        print(
            f"{task.title}: importance {task.importance}, "
            f"{task.effort_h} h, due {task.deadline}"
        )


if __name__ == "__main__":
    main()
