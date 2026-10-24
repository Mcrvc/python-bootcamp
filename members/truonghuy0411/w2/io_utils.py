"""CSV and JSON I/O utilities for tasks."""

import csv
import json
from datetime import date
from pathlib import Path

from .models import Task


def load_tasks(path: str | Path) -> list[Task]:
    """Load task items from a CSV file."""
    taskList = []

    with open(path, mode="r", encoding="utf-8") as fileData:
        csvReader = csv.reader(fileData)
        next(csvReader, None)

        for rowData in csvReader:
            lineNum = csvReader.line_num

            if not rowData or len(rowData) != 4:
                raise ValueError(f"line {lineNum}: invalid column count")

            try:
                taskTitle = rowData[0].strip()
                taskImportance = int(rowData[1].strip())
                taskEffort = float(rowData[2].strip())
                taskDeadline = date.fromisoformat(rowData[3].strip())

                newTask = Task(
                    title=taskTitle,
                    importance=taskImportance,
                    effort_h=taskEffort,
                    deadline=taskDeadline,
                )
                taskList.append(newTask)
            except (ValueError, TypeError) as err:
                raise ValueError(f"line {lineNum}: {err}") from err

    return taskList


def save_json(tasks: list[Task], path: str | Path) -> None:
    """Save task items to a JSON file."""
    dataList = []
    for currentTask in tasks:
        taskDict = {
            "title": currentTask.title,
            "importance": currentTask.importance,
            "effort_h": currentTask.effort_h,
            "deadline": str(currentTask.deadline),
        }
        dataList.append(taskDict)

    with open(path, mode="w", encoding="utf-8") as outputFile:
        json.dump(dataList, outputFile, indent=4)