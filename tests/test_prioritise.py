from datetime import date, timedelta
import pytest
from shared.contract import Task
from shared.study_planner.prioritise import prioritise, generate_blocks

def test_prioritise_happy_case():
    today = date(2026, 10, 13)
    task_low = Task(title="Low Priority", importance=2, effort_h=2.0, deadline=today + timedelta(days=10))
    task_high = Task(title="High Priority", importance=5, effort_h=1.0, deadline=today + timedelta(days=1))
    prioritized = prioritise([task_low, task_high], today)
    assert prioritized[0].title == "High Priority"
    assert prioritized[1].title == "Low Priority"

def test_generate_blocks_edge_cases():
    today = date(2026, 10, 13)
    task_due_today = Task(title="Due Today", importance=4, effort_h=3.0, deadline=today)
    task_overdue = Task(title="Overdue", importance=5, effort_h=2.0, deadline=today - timedelta(days=2))
    blocks_zero = generate_blocks([task_due_today, task_overdue], today, daily_capacity_h=0.0)
    assert len(blocks_zero) == 0
    blocks_partial = generate_blocks([task_due_today, task_overdue], today, daily_capacity_h=1.5)
    assert len(blocks_partial) == 1
    assert blocks_partial[0].task.title == "Overdue"
    assert blocks_partial[0].hours == 1.5

def test_prioritise_error_invalid_input():
    today = date(2026, 10, 13)
    with pytest.raises(TypeError):
        prioritise(None, today)  # type: ignore