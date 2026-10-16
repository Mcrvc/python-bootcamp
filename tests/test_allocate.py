import pytest
from datetime import date
from shared.contract import Task
from shared.study_planner.allocate import allocate


# 1. Happy tests
def test_allocate_happy_path():
    t1 = Task(title="Math", importance=5, effort_h=2.0, deadline=date(2026, 10, 20))
    t2 = Task(title="Physics", importance=4, effort_h=3.0, deadline=date(2026, 10, 21))
    t3 = Task(title="Chemistry", importance=3, effort_h=4.0, deadline=date(2026, 10, 22))

    blocks = allocate([t1, t2, t3], hours=5.0)

    assert len(blocks) == 2
    assert blocks[0].task.title == "Math"
    assert blocks[0].hours == 2.0
    assert blocks[1].task.title == "Physics"
    assert blocks[1].hours == 3.0


def test_allocate_skips_task_that_exceeds_remaining_hours():
    t1 = Task(title="Small 1", importance=5, effort_h=2.0, deadline=date(2026, 10, 20))
    t2 = Task(title="Too Big", importance=4, effort_h=5.0, deadline=date(2026, 10, 21))
    t3 = Task(title="Small 2", importance=3, effort_h=1.0, deadline=date(2026, 10, 22))

    blocks = allocate([t1, t2, t3], hours=3.0)

    assert len(blocks) == 2
    assert [b.task.title for b in blocks] == ["Small 1", "Small 2"]


# 2. Edge tests
def test_allocate_edge_zero_hours():
    t1 = Task(title="History", importance=2, effort_h=1.0, deadline=date(2026, 10, 20))
    assert allocate([t1], hours=0.0) == []


def test_allocate_edge_empty_tasks():
    assert allocate([], hours=10.0) == []


def test_allocate_edge_zero_effort_task():
    t0 = Task(title="Zero Task", importance=1, effort_h=0.0, deadline=date(2026, 10, 20))
    t1 = Task(title="Real Task", importance=5, effort_h=2.0, deadline=date(2026, 10, 20))
    blocks = allocate([t0, t1], hours=3.0)
    assert len(blocks) == 1
    assert blocks[0].task.title == "Real Task"


# 3. Error tests
def test_allocate_error_negative_hours():
    t1 = Task(title="Math", importance=5, effort_h=2.0, deadline=date(2026, 10, 20))
    with pytest.raises(ValueError):
        allocate([t1], hours=-1.0)


def test_allocate_error_negative_task_effort():
    t_invalid = Task(title="Bad Task", importance=3, effort_h=-2.0, deadline=date(2026, 10, 20))
    with pytest.raises(ValueError):
        allocate([t_invalid], hours=5.0)