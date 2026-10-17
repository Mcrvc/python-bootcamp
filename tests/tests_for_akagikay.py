"""W2-4 cross-tests by truonghuy0411 for member (akagikay) W1 functions.

Run with: pytest tests/tests_for_akagikay.py (from the repo root).
"""

import sys
from pathlib import Path

import pytest

BOOTCAMP = Path(__file__).resolve().parents[1]
if str(BOOTCAMP) not in sys.path:
    sys.path.insert(0, str(BOOTCAMP))

from members.akagikay.w1 import grades, rules, text_tools, timetable  # noqa: E402
from members.akagikay.w1.translate import insertion_sort  # noqa: E402



def test_summary_values():
    sampleScores = [6.0, 7.0, 8.0, 9.0]
    summaryResult = grades.summary(sampleScores)
    assert summaryResult["min"] == 6.0
    assert summaryResult["max"] == 9.0
    assert summaryResult["mean"] == 7.5
    assert summaryResult["median"] == 7.5


def test_summary_empty_raises():
    with pytest.raises(ValueError):
        grades.summary([])


def test_summary_does_not_change_input():
    inputScores = [8.0, 6.0, 9.0, 7.5]
    grades.summary(inputScores)
    assert inputScores == [8.0, 6.0, 9.0, 7.5]



def test_top_k_tie_goes_alphabetical():
    assert text_tools.top_k("is git is git", 2) == [("git", 2), ("is", 2)]


def test_top_k_empty_string():
    assert text_tools.top_k("", 3) == []


def test_can_register_boundaries():
    assert rules.can_register_thesis(120, 2.0) is True
    assert rules.can_register_thesis(119, 4.0) is False
    assert rules.can_register_thesis(200, 1.99) is False


def test_missing_messages():
    assert rules.missing(118, 3.1) == ["need 2 more credits"]
    assert rules.missing(120, 2.0) == []



def test_by_day_groups_and_sorts():
    rawSchedule = [
        ("CSC10014", "Mon"),
        ("MTH00003", "Tue"),
        ("CSC10001", "Mon"),
    ]
    groupedSchedule = timetable.by_day(rawSchedule)
    assert groupedSchedule == {
        "Mon": ["CSC10001", "CSC10014"],
        "Tue": ["MTH00003"],
    }
    assert timetable.by_day([]) == {}


def test_insertion_sort_negative_and_zero():
    mixedList = [0, -10, 5, -3, 2, -1, 0, 8]
    expectedList = [-10, -3, -1, 0, 0, 2, 5, 8]
    assert insertion_sort(mixedList) == expectedList


def test_insertion_sort_in_place_modification():
    originalList = [5, 1, 4, 2, 8]
    returnedList = insertion_sort(originalList)
    assert returnedList == [1, 2, 4, 5, 8]
    assert originalList == [1, 2, 4, 5, 8]
    assert returnedList is originalList