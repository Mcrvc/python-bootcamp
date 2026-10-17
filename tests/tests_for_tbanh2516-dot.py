import pytest

from members.tbanh2516_dot.w1.grades import summary
from members.tbanh2516_dot.w1.text_tools import word_count, top_k
from members.tbanh2516_dot.w1.rules import can_register_thesis, missing
from members.tbanh2516_dot.w1.translate import is_palindrome
from members.tbanh2516_dot.w1.timetable import by_day


#W1-1

def test_summary_basic():
    assert summary([7.5,9,6,8]) == {"min": 6, "max": 9, "mean": 7.62, "median": 7.75}

def test_summary_odd_count():
    assert summary([1,2,3]) == {"min": 1, "max": 3, "mean": 2, "median": 2}

def test_summary_one_element():
    assert summary([5]) == {"min": 5, "max": 5, "mean": 5, "median": 5}

def test_summary_all_equal_values():
    assert summary([3,3,3,3]) == {"min": 3, "max": 3, "mean": 3, "median": 3}

def test_summary_empty_raises():
    with pytest.raises(ValueError):
        summary([])

#W1-2

def test_word_count_basic():
    assert word_count("Git is fun. Git is fast!") == {"git": 2, "is": 2, "fun": 1, "fast": 1}

def test_word_count_lowercases():
    assert word_count("Hello HELLO hello") == {"hello": 3}

def test_word_count_empty_string():
    assert word_count("") == {}

def test_word_count_whitespace_only():
    assert word_count("   ") == {}

def test_top_k_basic():
    assert top_k("Git is fun. Git is fast!", 2) == [("git", 2), ("is", 2)]

def test_top_k_sorted_by_count_descending():
    assert top_k("a a a b b c", 3) == [("a", 3), ("b", 2), ("c", 1)]

def test_top_k_k_larger_than_distinct():
    assert top_k("one two three", 10) == [("one", 1), ("three", 1), ("two", 1)]

def test_top_k_tie_at_cutoff_shuffled():
    assert top_k("d d c c b b a a", 3) == [("a", 2), ("b", 2), ("c", 2)]

#W1-3

def test_can_register_thesis_boundary_pass():
    assert can_register_thesis(120,2.0) is True

def test_can_register_thesis_boundary_fail_credits():
    assert can_register_thesis(119, 2.0) is False

def test_can_register_thesis_zero():
    assert can_register_thesis(0, 0.0) is False

def test_missing_eligible_returns_empty():
    assert missing(120, 2.0) == []

def test_missing_needs_credits_only():
    assert missing(119, 2.0) == ["need 1 more credits"]

def test_missing_needs_gpa_only():
    assert missing(120, 1.99) == ["need GPA of at least 2.0"]

def test_missing_extreme_fail():
    assert missing(0,0.0) == ["need 120 more credits", "need GPA of at least 2.0"]

#W1-4

def test_simple_palindrome():
    assert is_palindrome("abcba") is True

def test_simple_non_palindrome():
    assert is_palindrome("hello") is False

def test_uppercase_palindrome():
    assert is_palindrome("ABCBA") is True

def test_uppercase_non_palindrome():
    assert is_palindrome("HELLO") is False

def test_ignores_case_and_punctuation():
    assert is_palindrome("A man, a plan, a canal: Panama") is True

def test_empty_string():
    assert is_palindrome("") is True

def test_single_character():
    assert is_palindrome("a") is True

def test_alphanumeric_palindrome():
    assert is_palindrome("A1b2b1a") is True

def test_only_punctuation():
    assert is_palindrome("!!!") is True

#W1-5

def test_by_day_basic():
    assert by_day([
        ("CSC10014", "Mon"),
        ("MTH00003", "Tue"),
        ("CSC10001", "Mon"),
    ]) == {
        "Mon": ["CSC10001", "CSC10014"],
        "Tue": ["MTH00003"],
    }

def test_by_day_single_pair():
    assert by_day([("CSC10014", "Mon")]) == {"Mon": ["CSC10014"]}

def test_by_day_empty_list():
    assert by_day([]) == {}

def test_by_day_sorts_courses_within_day():
    assert by_day([
        ("Z", "Mon"),
        ("A", "Mon"),
        ("M", "Mon"),
    ]) == {"Mon": ["A", "M", "Z"]}

def test_by_day_multiple_days_isolated():
    assert by_day([
        ("CSC10014", "Mon"),
        ("MTH00003", "Tue"),
        ("CSC10001", "Mon"),
        ("PHY00001", "Wed"),
    ]) == {
        "Mon": ["CSC10001", "CSC10014"],
        "Tue": ["MTH00003"],
        "Wed": ["PHY00001"],
    }