from members.Mcrvc.w1.grades import summary
from members.Mcrvc.w1.rules import can_register_thesis, missing
from members.Mcrvc.w1.text_tools import top_k, word_count
from members.Mcrvc.w1.timetable import by_day
from members.Mcrvc.w1.translate import binary_search


def test_normal_list():
    inputList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert (binary_search(inputList, 5) == 4)


def test_empty_list():
    inputList = []
    assert (binary_search(inputList, 0) == -1)


def test_key_at_start():
    inputList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert binary_search(inputList, 1) == 0


def test_key_at_end():
    inputList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert binary_search(inputList, 10) == 9


def test_key_at_middle():
    inputList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert binary_search(inputList, 6) == 5


def test_key_at_middle2():
    inputList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert binary_search(inputList, 5) == 4


def test_binary_search_not_found():
    inputList = [1, 3, 5, 7, 9]
    assert binary_search(inputList, 4) == -1
    assert binary_search(inputList, 10) == -1
    assert binary_search(inputList, 0) == -1


def test_binary_search_single_element():
    assert binary_search([42], 42) == 0
    assert binary_search([42], 7) == -1


def test_summary_normal():
    assert summary([7.5, 9, 6, 8]) == {
        "min": 6,
        "max": 9,
        "mean": 7.62,
        "median": 7.75,
    }


def test_summary_single_element():
    assert summary([5]) == {"min": 5, "max": 5, "mean": 5, "median": 5}


def test_summary_even_count():
    assert summary([1, 2, 3, 4]) == {
        "min": 1,
        "max": 4,
        "mean": 2.5,
        "median": 2.5,
    }


def test_summary_empty_raises():
    try:
        summary([])
    except ValueError:
        pass
    else:
        raise AssertionError("expected ValueError for empty list")


def test_can_register_thesis_eligible():
    assert can_register_thesis(120, 2.0) is True
    assert can_register_thesis(150, 3.5) is True


def test_can_register_thesis_not_eligible():
    assert can_register_thesis(118, 3.1) is False  # credits only
    assert can_register_thesis(120, 1.9) is False  # gpa only
    assert can_register_thesis(100, 1.5) is False  # both


def test_missing_eligible():
    assert missing(120, 2.0) == []
    assert missing(150, 3.5) == []


def test_missing_credits_only():
    assert missing(118, 3.1) == ["need 2 more credits"]


def test_missing_gpa_only():
    assert missing(120, 1.5) == ["need 0.5 more GPA"]


def test_missing_both():
    assert len(missing(100, 1.5)) == 2
    assert "need 20 more credits" in missing(100, 1.5)


def test_word_count_basic():
    assert word_count("Git is fun. Git is fast!") == {
        "git": 2,
        "is": 2,
        "fun": 1,
        "fast": 1,
    }


def test_word_count_case_insensitive():
    assert word_count("Python PYTHON python") == {"python": 3}


def test_word_count_punctuation():
    assert word_count("Hello, world! Hello?") == {"hello": 2, "world": 1}


def test_word_count_empty():
    assert word_count("") == {}


def test_top_k():
    assert top_k("Git is fun. Git is fast!", 2) == [("git", 2), ("is", 2)]


def test_top_k_k_zero_or_negative():
    assert top_k("a b c", 0) == []
    assert top_k("a b c", -1) == []


def test_top_k_empty_text():
    assert top_k("", 3) == []


def test_top_k_k_larger_than_unique():
    assert top_k("a b a", 5) == [("a", 2), ("b", 1)]


def test_by_day_groups_and_sorts():
    pairs = [
        ("CSC10014", "Mon"),
        ("MTH00003", "Tue"),
        ("CSC10001", "Mon"),
    ]
    assert by_day(pairs) == {
        "Mon": ["CSC10001", "CSC10014"],
        "Tue": ["MTH00003"],
    }


def test_by_day_empty():
    assert by_day([]) == {}
