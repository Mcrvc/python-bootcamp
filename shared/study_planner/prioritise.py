from datetime import date
from typing import List
from shared.contract import Task, Block

def prioritise(tasks: List[Task], today: date) -> List[Task]:
    def get_priority_score(task: Task) -> float:
        return task.importance / max(1,(task.deadline - today).days)

    return sorted(tasks, key=get_priority_score, reverse=True)

def generate_blocks(tasks: List[Task], today: date, daily_capacity_h: float) -> List[Block]:
    prioritized = prioritise(tasks, today)
    blocks: List[Block] = []
    remaining_capacity = daily_capacity_h
    for task in prioritized:
        if remaining_capacity <= 0:
            break
        allocated_hours = min(task.effort_h, remaining_capacity)
        blocks.append(Block(task=task, hours=allocated_hours))
        remaining_capacity -= allocated_hours

    return blocks