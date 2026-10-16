from datetime import date, timedelta

import pytest

from shared.contract import Task
from shared.study_planner.filter import filter_upcoming

@pytest.fixture
def today() -> date:
    return date(2026, 10, 26)


@pytest.fixture
def tasks() -> list[Task]:
    return [
        Task("Overdue",     5, 2.0, date(2026, 10, 20)),
        Task("Due today",   4, 1.0, date(2026, 10, 26)),
        Task("In 3 days",   3, 1.5, date(2026, 10, 29)),
        Task("On the edge", 2, 2.0, date(2026, 11, 2)),
        Task("Too far",     1, 0.5, date(2026, 11, 10)),
    ]

#Happy Path

def test_filter_upcoming_keeps_tasks_within_window(today, tasks):
    result = filter_upcoming(tasks, today, days=7)
    assert [t.title for t in result] == ["Due today", "In 3 days", "On the edge"]


def test_filter_upcoming_preserves_input_order(today):
    ordered = [
        Task("Later",  3, 1.0, date(2026, 10, 28)),
        Task("Sooner", 3, 1.0, date(2026, 10, 27)),
    ]
    result = filter_upcoming(ordered, today, days=7)
    assert [t.title for t in result] == ["Later", "Sooner"]

#Edge cases

def test_filter_upcoming_empty_input_returns_empty(today):
    assert filter_upcoming([], today, days=7) == []


def test_filter_upcoming_days_zero_only_today(today, tasks):
    result = filter_upcoming(tasks, today, days=0)
    assert [t.title for t in result] == ["Due today"]


def test_filter_upcoming_includes_both_boundaries(today):
    boundary = [
        Task("First day", 3, 1.0, today),
        Task("Last day",  3, 1.0, today + timedelta(days=7)),
    ]
    result = filter_upcoming(boundary, today, days=7)
    assert len(result) == 2


def test_filter_upcoming_drops_overdue_tasks(today, tasks):
    result = filter_upcoming(tasks, today, days=7)
    assert "Overdue" not in {t.title for t in result}


def test_filter_upcoming_does_not_mutate_input(today, tasks):
    snapshot = list(tasks)
    filter_upcoming(tasks, today, days=7)
    assert tasks == snapshot

#Error cases

def test_filter_upcoming_negative_days_raises(today, tasks):
    with pytest.raises(ValueError, match="days"):
        filter_upcoming(tasks, today, days=-1)