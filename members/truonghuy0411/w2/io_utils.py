import csv
from datetime import date
import json

from .models import Task


def load_tasks(path) -> list[Task]:
    taskList = []

    with open(path, mode="r", encoding="utf-8") as fileData:
        csvReader = csv.reader(fileData)
        next(csvReader, None) 

        for rowData in csvReader:
            lineNum = csvReader.line_num

            if not rowData or len(rowData) != 4:
                raise ValueError(f"Line {lineNum}: so luong cot khong hop le")

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
            except Exception as err:
                raise ValueError(f"Line {lineNum}: {err}")

    return taskList


def save_json(tasks: list[Task], path) -> None:
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