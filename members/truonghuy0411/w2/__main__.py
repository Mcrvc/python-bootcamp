import os
from .io_utils import load_tasks


def main():
    sampleCsvPath = "samples/tasks.csv"

    if not os.path.exists(sampleCsvPath):
        rootDir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
        sampleCsvPath = os.path.join(rootDir, "samples", "tasks.csv")

    loadedTasks = load_tasks(sampleCsvPath)
    for taskItem in loadedTasks:
        print(taskItem)


if __name__ == "__main__":
    main()