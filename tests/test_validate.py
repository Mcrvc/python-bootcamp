from datetime import date

import pytest

from shared.contract import Task
from shared.study_planner.validate import validate

TODAY = date(2026, 10, 26)


# Happy path
def test_keeps_valid_and_drops_invalid():
    tasks = [
        Task("ok", 3, 2.0, date(2026, 10, 30)),
        Task("overdue", 3, 2.0, date(2026, 10, 20)),
        Task("negative effort", 3, -1.0, date(2026, 10, 30)),
        Task("bad importance", 9, 2.0, date(2026, 10, 30)),
    ]
    assert [t.title for t in validate(tasks, TODAY)] == ["ok"]


# Edge cases
def test_due_today_is_kept():
    task = Task("today", 3, 1.0, TODAY)
    assert validate([task], TODAY) == [task]


def test_importance_boundaries_kept():
    tasks = [
        Task("low", 1, 1.0, date(2026, 10, 30)),
        Task("high", 5, 1.0, date(2026, 10, 30)),
    ]
    assert [t.title for t in validate(tasks, TODAY)] == ["low", "high"]


def test_zero_effort_is_kept():
    assert validate([Task("zero", 3, 0.0, date(2026, 10, 30))], TODAY) == [Task("zero", 3, 0.0, date(2026, 10, 30))]


def test_empty_list():
    assert validate([], TODAY) == []


def test_input_not_modified():
    tasks = [Task("overdue", 3, 2.0, date(2026, 10, 20))]
    validate(tasks, TODAY)
    assert len(tasks) == 1


# Error case
def test_today_must_be_date():
    with pytest.raises(TypeError):
        validate([], "2026-10-26")

