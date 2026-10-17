import pytest
from members.ILoveCats123abc.w1 import grades, rules, text_tools, timetable
from members.ILoveCats123abc.w1.translate import reverse_array

# ==========================================
# 1. W1-1: grades.py (summary)
# ==========================================
def test_summary_happy():
    scores = [7.5, 9, 6, 8]
    assert grades.summary(scores) == {
        "min": 6,
        "max": 9,
        "mean": 7.62,
        "median": 7.75,
    }


def test_summary_empty_raises_value_error():
    with pytest.raises(ValueError):
        grades.summary([])


def test_summary_single_element():
    assert grades.summary([5.0]) == {
        "min": 5.0,
        "max": 5.0,
        "mean": 5.0,
        "median": 5.0,
    }


# ==========================================
# 2. W1-2: text_tools.py (word_count, top_k)
# ==========================================
def test_word_count_clean_punctuation():
    text = "Git is fun. Git is fast!"
    assert text_tools.word_count(text) == {
        "git": 2,
        "is": 2,
        "fun": 1,
        "fast": 1,
    }


def test_top_k_sorting_and_tie_break():
    assert text_tools.top_k("is git is git", 2) == [("git", 2), ("is", 2)]
    assert text_tools.top_k("a b c", 0) == []


# ==========================================
# 3. W1-3: rules.py (can_register_thesis, missing)
# ==========================================
def test_can_register_thesis_boundary():
    assert rules.can_register_thesis(120, 2.0) is True
    assert rules.can_register_thesis(119, 3.0) is False
    assert rules.can_register_thesis(130, 1.9) is False


def test_missing_reasons_formatting():
    assert rules.missing(118, 1.8) == [
        "need 2 more credits",
        "need 0.2 more gpa",
    ]
    assert rules.missing(120, 2.0) == []


# ==========================================
# 4. W1-5: timetable.py (by_day - Bộ test mở rộng)
# ==========================================
def test_by_day_groups_and_sorts_courses():
    """Test gom nhóm môn học theo ngày và sắp xếp tên môn học theo bảng chữ cái."""
    pairs = [("CSC10014", "Mon"), ("MTH00003", "Tue"), ("CSC10001", "Mon")]
    got = timetable.by_day(pairs)
    assert got == {"Mon": ["CSC10001", "CSC10014"], "Tue": ["MTH00003"]}


def test_by_day_empty_input():
    """Edge case: Danh sách danh mục rỗng."""
    assert timetable.by_day([]) == {}


def test_by_day_single_course():
    """Edge case: Chỉ có 1 môn học."""
    assert timetable.by_day([("PHY10001", "Wed")]) == {"Wed": ["PHY10001"]}


def test_by_day_multiple_courses_same_day_sorting():
    """Test kiểm tra sắp xếp thứ tự bảng chữ cái khi có nhiều môn trong cùng 1 ngày."""
    pairs = [("ZOO101", "Fri"), ("ALG202", "Fri"), ("BIO101", "Fri")]
    got = timetable.by_day(pairs)
    assert got == {"Fri": ["ALG202", "BIO101", "ZOO101"]}


def test_by_day_does_not_modify_input():
    """Test đảm bảo hàm không làm thay đổi (mutate) danh sách tuple đầu vào."""
    pairs = [("CSC10014", "Mon"), ("MTH00003", "Tue")]
    original = list(pairs)
    timetable.by_day(pairs)
    assert pairs == original


# ==========================================
# 5. W1-4: translate.py (reverse_array - Bộ test mở rộng)
# ==========================================
def test_reverse_even_elements():
    arr = [1, 2, 3, 4]
    assert reverse_array(arr) == [4, 3, 2, 1]


def test_reverse_odd_elements():
    arr = [1, 2, 3, 4, 5]
    assert reverse_array(arr) == [5, 4, 3, 2, 1]


def test_reverse_empty_array():
    arr = []
    assert reverse_array(arr) == []


def test_reverse_single_element():
    arr = [42]
    assert reverse_array(arr) == [42]


def test_reverse_two_elements():
    arr = [10, 20]
    assert reverse_array(arr) == [20, 10]


def test_reverse_with_negative_and_duplicates():
    arr = [-5, 2, 2, -10]
    assert reverse_array(arr) == [-10, 2, 2, -5]


def test_reverse_all_identical_elements():
    arr = [7, 7, 7, 7]
    assert reverse_array(arr) == [7, 7, 7, 7]


def test_reverse_large_array():
    arr = list(range(1000))
    expected = list(reversed(range(1000)))
    assert reverse_array(arr) == expected


def test_in_place_mutation():
    arr = [1, 2, 3]
    original_id = id(arr)
    result = reverse_array(arr)
    assert id(result) == original_id
    assert arr == [3, 2, 1]