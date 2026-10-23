from datetime import date
from shared.contract import Task, Block
from shared.study_planner.stats import calculate_stats

def test_calculate_stats_basic():
    today = date(2026, 10, 26)

    t1 = Task("Math", 5, 2.0, date(2026, 10, 27))
    t2 = Task("History", 3, 1.0, date(2026, 10, 25))
    t3 = Task("Physics", 4, 3.0, date(2026, 10, 28))

    all_tasks = [t1, t2, t3]
    blocks = [
        Block(task=t1, hours=2.0),
        Block(task=t3, hours=1.0),
    ]

    stats = calculate_stats(blocks, available_hours=3.0, today=today, all_tasks=all_tasks)

    assert stats["total_allocated_hours"] == 3.0
    assert stats["available_hours"] == 3.0
    assert stats["allocation_percentage"] == 100.0
    assert stats["tasks_scheduled"] == 2
    assert stats["total_tasks"] == 3
    assert stats["completion_percentage"] == 66.67
    assert stats["skipped_overdue_count"] == 1

def test_calculate_stats_empty():
    today = date(2026, 10, 26)
    stats = calculate_stats([], available_hours=0, today=today, all_tasks=[])

    assert stats["allocation_percentage"] == 0.0
    assert stats["completion_percentage"] == 0.0
    assert stats["skipped_overdue_count"] == 0