"""W1-4 (member 5) Palindrome check.

Problem: Write a function that returns True if a string reads the same
forwards and backwards, ignoring case and non-alphanumeric characters;
otherwise return False.

C++ vs Python: in C++ we compare characters with two indices moving
toward the middle; in Python we can reverse a string with slicing
(s[::-1]) and compare it with the original.
"""


def is_palindrome(s: str) -> bool:
    s = s.lower()
    s = ''.join(ch for ch in s if ch.isalnum())
    return s == s[::-1]