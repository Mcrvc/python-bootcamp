"""Tests for shared.study_planner.store."""

import json
from datetime import date

import pytest

from shared.contract import Block, Task
from shared.study_planner.store import save_json


def make_block(
    title: str = "Calculus assignment",
    importance: int = 4,
    effort_h: float = 2.5,
    deadline: date = date(2026, 10, 30),
    hours: float = 1.5,
) -> Block:
    """Create a sample block for testing."""
    task = Task(
        title=title,
        importance=importance,
        effort_h=effort_h,
        deadline=deadline,
    )
    return Block(task=task, hours=hours)


def test_save_json_writes_valid_schedule(tmp_path):
    """Happy path: save blocks and verify their JSON representation."""
    blocks = [
        make_block(),
        make_block(
            title="Physics revision",
            importance=5,
            effort_h=3.0,
            deadline=date(2026, 11, 2),
            hours=2.0,
        ),
    ]
    output = tmp_path / "schedule.json"

    result = save_json(blocks, output)

    assert result is None
    assert output.is_file()

    data = json.loads(output.read_text(encoding="utf-8"))

    assert len(data) == 2
    assert data[0] == {
        "task": {
            "title": "Calculus assignment",
            "importance": 4,
            "effort_h": 2.5,
            "deadline": "2026-10-30",
        },
        "hours": 1.5,
    }
    assert data[1]["task"]["title"] == "Physics revision"
    assert data[1]["task"]["deadline"] == "2026-11-02"
    assert data[1]["hours"] == 2.0


def test_save_json_handles_empty_blocks(tmp_path):
    """Edge case: an empty schedule should become an empty JSON array."""
    output = tmp_path / "empty_schedule.json"

    save_json([], output)

    assert output.is_file()
    assert json.loads(output.read_text(encoding="utf-8")) == []


def test_save_json_raises_for_missing_parent_directory(tmp_path):
    """Error case: do not silently create a missing parent directory."""
    output = tmp_path / "missing" / "schedule.json"

    with pytest.raises(FileNotFoundError):
        save_json([make_block()], output)

    assert not output.exists()


def test_save_json_preserves_unicode(tmp_path):
    """Unicode task titles should survive a save-and-load round trip."""
    output = tmp_path / "unicode_schedule.json"
    blocks = [make_block(title="Ôn tập Giải tích")]

    save_json(blocks, output)

    raw_json = output.read_text(encoding="utf-8")
    data = json.loads(raw_json)

    assert "Ôn tập Giải tích" in raw_json
    assert data[0]["task"]["title"] == "Ôn tập Giải tích"


def test_save_json_overwrites_existing_file(tmp_path):
    """Saving a new schedule should replace the previous file contents."""
    output = tmp_path / "schedule.json"
    output.write_text('{"old": true}', encoding="utf-8")

    save_json([make_block(title="New task")], output)

    data = json.loads(output.read_text(encoding="utf-8"))

    assert len(data) == 1
    assert data[0]["task"]["title"] == "New task"
    assert "old" not in data[0]
