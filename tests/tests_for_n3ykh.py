"""W2-4 cross-tests by Mcrvc for member 7 (n3ykh) W1 functions.

Run with: pytest tests/test_w1_7.py (from the repo root).
"""
import sys
from pathlib import Path

BOOTCAMP = Path(__file__).resolve().parents[1]
if str(BOOTCAMP) not in sys.path:
    sys.path.insert(0, str(BOOTCAMP))

import pytest

from members.n3ykh.w1 import grades, rules, text_tools, timetable
from members.n3ykh.w1.translate import sum_of_int


def test_summary_values():
    got = grades.summary([7.5, 9, 6, 8])
    assert got == {"min": 6, "max": 9, "mean": 7.62, "median": 7.75}


def test_summary_empty_raises():
    with pytest.raises(ValueError):
        grades.summary([])


def test_summary_does_not_change_input():
    scores = [8.0, 6.0, 9.0, 7.5]
    grades.summary(scores)
    assert scores == [8.0, 6.0, 9.0, 7.5]


def test_top_k_tie_goes_alphabetical():
    assert text_tools.top_k("is git is git", 2) == [("git", 2), ("is", 2)]


def test_top_k_negative_k_is_empty():
    assert text_tools.top_k("a b c", -1) == []


def test_can_register_boundaries():
    assert rules.can_register_thesis(120, 2.0) is True
    assert rules.can_register_thesis(119, 4.0) is False
    assert rules.can_register_thesis(200, 1.99) is False


def test_missing_messages():
    assert rules.missing(118, 3.1) == ["need 2 more credits"]
    assert rules.missing(120, 2.0) == []


def test_sum_of_int():
    assert sum_of_int(123) == 6
    assert sum_of_int(0) == 0
    assert sum_of_int(-456) == 15


def test_by_day_groups_and_sorts():
    got = timetable.by_day([("CSC10014", "Mon"), ("MTH00003", "Tue"), ("CSC10001", "Mon")])
    assert got == {"Mon": ["CSC10001", "CSC10014"], "Tue": ["MTH00003"]}
    assert timetable.by_day([]) == {}
