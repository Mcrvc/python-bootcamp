from members.truonghuy0411.w1.grades import summary
from members.truonghuy0411.w1.rules import can_register_thesis, missing
from members.truonghuy0411.w1.text_tools import top_k, word_count
from members.truonghuy0411.w1.timetable import by_day
from members.truonghuy0411.w1.translate import transpose


def test_summary_with_negative_scores():
    assert summary([-2, 0, 2]) == {
        "min": -2,
        "max": 2,
        "mean": 0,
        "median": 0,
    }


def test_word_count_with_only_punctuation_between_words():
    assert word_count("Hello... HELLO???") == {"hello": 2}


def test_top_k_breaks_ties_alphabetically():
    assert top_k("banana apple cherry", 2) == [("apple", 1), ("banana", 1)]


def test_thesis_rejects_low_gpa_with_enough_credits():
    assert not can_register_thesis(130, 1.5)
    assert missing(130, 1.5) == ["need 0.5 more gpa"]


def test_transpose_single_row():
    assert transpose([[1, 2, 3]]) == [[1], [2], [3]]


def test_by_day_sorts_multiple_courses():
    timetable = [
        ("MTH00003", "Mon"),
        ("CSC10014", "Mon"),
        ("PHY00001", "Tue"),
    ]

    assert by_day(timetable) == {
        "Mon": ["CSC10014", "MTH00003"],
        "Tue": ["PHY00001"],
    }
