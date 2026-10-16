from members.tbanh2516_dot.w1.translate import is_palindrome


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