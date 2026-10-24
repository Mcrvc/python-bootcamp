def can_register_thesis(credits: int, gpa: float) -> bool:
    """Return whether a student meets the thesis requirements."""
    return credits >= 120 and gpa >= 2.0


def missing(credits: int, gpa: float) -> list[str]:
    """Describe any credits or GPA missing from thesis requirements."""
    result: list[str] = []

    if credits < 120:
        needed = 120 - credits
        result.append(f"need {needed} more credits")

    if gpa < 2.0:
        needed_gpa = 2 - gpa
        result.append(f"need {needed_gpa:.2f} more GPA")

    return result
