from datetime import date
from typing import List
from ..contract import Task, Block

def calculate_stats(
    blocks: List[Block],
    available_hours: float,
    today: date,
    all_tasks: List[Task],
) -> dict:
    """Calculate execution metrics for the study planner.

    Args:
        blocks: List of allocated study blocks (each with a task and hours).
        available_hours: Total hours available for this study session.
        today: Current date, used to detect overdue tasks.
        all_tasks: The full list of tasks before allocation.

    Returns:
        A dict with the following keys:
            - total_allocated_hours (float): Sum of hours across all blocks.
            - available_hours (float): The input available_hours.
            - allocation_percentage (float): total_allocated / available_hours * 100.
            - tasks_scheduled (int): Number of unique tasks that got at least one block.
            - total_tasks (int): Total number of tasks in all_tasks.
            - completion_percentage (float): tasks_scheduled / total_tasks * 100.
            - skipped_overdue_count (int): Tasks with no block and deadline < today.
    """

    total_allocated = sum(block.hours for block in blocks)

    allocation_percentage = (
        (total_allocated / available_hours * 100) if available_hours > 0 else 0.0
    )

    scheduled_titles = {block.task.title for block in blocks}
    tasks_scheduled = len(scheduled_titles)
    total_tasks = len(all_tasks)
    completion_percentage = (
        (tasks_scheduled / total_tasks * 100) if total_tasks > 0 else 0.0
    )

    skipped_overdue = sum(
        1
        for task in all_tasks
        if task.title not in scheduled_titles and task.deadline < today
    )

    return {
        "total_allocated_hours": total_allocated,
        "available_hours": available_hours,
        "allocation_percentage": round(allocation_percentage, 2),
        "tasks_scheduled": tasks_scheduled,
        "total_tasks": total_tasks,
        "completion_percentage": round(completion_percentage, 2),
        "skipped_overdue_count": skipped_overdue,
    }