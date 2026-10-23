import json
from datetime import date
from pathlib import Path

import pytest

from shared.contract import Block
from shared.study_planner.allocate import allocate
from shared.study_planner.filter import filter_upcoming
from shared.study_planner.parse import parse_csv
from shared.study_planner.prioritise import generate_blocks, prioritise
from shared.study_planner.render import render
from shared.study_planner.store import save_json
from shared.study_planner.validate import validate

BOOTCAMP = Path(__file__).resolve().parents[1]
SAMPLES = BOOTCAMP / "samples"
GOOD_CSV = SAMPLES / "tasks.csv"
BAD_CSV = SAMPLES / "tasks_bad.csv"
TODAY = date(2026, 10, 26)


def run_pipeline(
    csv_path: str | Path,
    today: date,
    days: int,
    hours: float,
) -> list[Block]:
    valid = validate(parse_csv(csv_path), today)
    upcoming = filter_upcoming(valid, today, days)
    ordered = prioritise(upcoming, today)
    return allocate(ordered, hours)


def test_e2e_full_pipeline_with_sample_tasks(tmp_path):
    tasks = parse_csv(GOOD_CSV)
    assert [t.title for t in tasks] == ["DS exam", "Assignment"]
    assert tasks[0].deadline == date(2026, 10, 30)

    valid = validate(tasks, TODAY)
    assert [t.title for t in valid] == ["DS exam", "Assignment"]

    upcoming = filter_upcoming(valid, TODAY, days=7)
    assert [t.title for t in upcoming] == ["DS exam", "Assignment"]

    ordered = prioritise(upcoming, TODAY)
    assert [t.title for t in ordered] == ["Assignment", "DS exam"]

    blocks = allocate(ordered, hours=2.0)
    assert [(b.task.title, b.hours) for b in blocks] == [("Assignment", 1.5)]

    assert render(blocks) == "Tonight (1.5 h):\n1. Assignment: 1.5 h"

    output = tmp_path / "plan.json"
    save_json(blocks, output)
    assert json.loads(output.read_text(encoding="utf-8")) == [
        {
            "task": {
                "title": "Assignment",
                "importance": 4,
                "effort_h": 1.5,
                "deadline": "2026-10-27",
            },
            "hours": 1.5,
        }
    ]


def test_e2e_generous_budget_schedules_everything(tmp_path):
    blocks = run_pipeline(GOOD_CSV, TODAY, days=7, hours=10.0)

    assert [(b.task.title, b.hours) for b in blocks] == [
        ("Assignment", 1.5),
        ("DS exam", 6.0),
    ]
    assert render(blocks) == (
        "Tonight (7.5 h):\n"
        "1. Assignment: 1.5 h\n"
        "2. DS exam: 6.0 h"
    )

    output = tmp_path / "plan.json"
    save_json(blocks, output)
    data = json.loads(output.read_text(encoding="utf-8"))
    assert [entry["task"]["deadline"] for entry in data] == [
        "2026-10-27",
        "2026-10-30",
    ]


def test_e2e_filter_window_drops_far_deadline():
    blocks = run_pipeline(GOOD_CSV, TODAY, days=1, hours=5.0)

    assert [b.task.title for b in blocks] == ["Assignment"]
    assert "DS exam" not in render(blocks)


def test_e2e_overdue_sample_task_is_dropped():
    later = date(2026, 10, 28)

    valid = validate(parse_csv(GOOD_CSV), later)
    assert [t.title for t in valid] == ["DS exam"]

    blocks = run_pipeline(GOOD_CSV, later, days=7, hours=6.0)
    assert [b.task.title for b in blocks] == ["DS exam"]
    assert render(blocks) == "Tonight (6.0 h):\n1. DS exam: 6.0 h"


def test_e2e_empty_plan_after_all_deadlines(tmp_path):
    after_all = date(2026, 11, 1)

    blocks = run_pipeline(GOOD_CSV, after_all, days=7, hours=5.0)

    assert blocks == []
    assert render(blocks) == "No tasks scheduled."

    output = tmp_path / "empty_plan.json"
    save_json(blocks, output)
    assert json.loads(output.read_text(encoding="utf-8")) == []


def test_e2e_generate_blocks_splits_leftover_capacity():
    tasks = validate(parse_csv(GOOD_CSV), TODAY)

    blocks = generate_blocks(tasks, TODAY, daily_capacity_h=2.0)

    assert [(b.task.title, b.hours) for b in blocks] == [
        ("Assignment", 1.5),
        ("DS exam", 0.5),
    ]
    assert render(blocks) == (
        "Tonight (2.0 h):\n"
        "1. Assignment: 1.5 h\n"
        "2. DS exam: 0.5 h"
    )


def test_e2e_corrupt_sample_fails_at_parse_stage():
    with pytest.raises(ValueError, match="Line 3"):
        parse_csv(BAD_CSV)
