from datetime import date

import pytest

from shared.contract import Block, Task
from shared.study_planner.render import render


def test_render_plan():
    assignment = Task("Assignment", 4, 1.5, date(2026, 10, 27))
    exam = Task("DS exam", 5, 6.0, date(2026, 10, 30))
    blocks = [Block(assignment, 1.5), Block(exam, 0.5)]

    assert render(blocks) == (
        "Tonight (2.0 h):\n"
        "1. Assignment: 1.5 h\n"
        "2. DS exam: 0.5 h"
    )


def test_render_empty_plan():
    assert render([]) == "No tasks scheduled."


def test_render_negative_hours():
    task = Task("Invalid task", 1, 1.0, date(2026, 10, 20))

    with pytest.raises(ValueError, match="non-negative"):
        render([Block(task, -1.0)])
