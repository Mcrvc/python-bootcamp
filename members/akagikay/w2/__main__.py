from pathlib import Path
from .io_utils import load_tasks


def main():
    csvp = Path(__file__).parent / "tasks.csv"

    if not csvp.exists():
        print("No sample csv found")
        return
    tasks = load_tasks(csvp)
    for i, task in enumerate(tasks, start = 1):
        print(f"Task {i}")
        print(f"\t{task.title}")
        print(f"\t{task.importance}")
        print(f"\t{task.effort_h}")
        print(f"\t{task.deadline}")

if __name__ == "__main__":
    main()
