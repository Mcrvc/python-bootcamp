from __future__ import annotations
from shared.contract import Task, Block

def allocate(tasks: list[Task], hours: float) -> list[Block]:
 
    if hours is None or hours < 0:
        raise ValueError("hours must be a non-negative number")

    if not tasks or hours == 0:
        return []

    blocks: list[Block] = []
    remaining_hours = float(hours)

    for task in tasks:
        if task.effort_h < 0:
            raise ValueError(f"Task '{task.title}' has invalid negative effort_h: {task.effort_h}")
        
        if task.effort_h == 0:
            continue

        if remaining_hours <= 1e-9:
            break

        if task.effort_h <= remaining_hours + 1e-9:
            blocks.append(Block(task=task, hours=task.effort_h))
            remaining_hours -= task.effort_h

    return blocks