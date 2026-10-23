"""Thesis eligibility rules."""

def can_register_thesis(credits: int, gpa: float) -> bool:
    """Return True if the student has enough credits and GPA to register."""
    return credits >= 120 and gpa >= 2.0


def missing(credits: int, gpa: float) -> list[str]:
    """Return human-readable reasons why the student cannot register yet."""
    reason: list[str] = []
    if credits < 120:
        needCre = 120 - credits
        reason.append(f"need {needCre} more credits")
    if gpa < 2.0:
        needGpa = round(2.0 - gpa, 2)
        reason.append(f"need {needGpa} more GPA")
    return reason
