"""w1-3: prerequisite rules for thesis registration"""

MIN_CREDITS = 120

MIN_GPA = 2.0


def can_register_thesis(credits: int, gpa: float) -> bool:
    """Return True if the student is eligible to register for a thesis."""
    return credits >= MIN_CREDITS and gpa >= MIN_GPA


def missing(credits: int, gpa: float) -> list[str]:
    """Return a list of unmet requirements."""
    reasons = []
    if credits < MIN_CREDITS:
        reasons.append(f"need {MIN_CREDITS - credits} more credits")
    if gpa < MIN_GPA:
        reasons.append(f"need GPA of at least {MIN_GPA}")
    return reasons
