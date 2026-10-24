"""Missing credits/gpa checker."""

def can_register_thesis(credits: int, gpa: float) -> bool:
    """Check whether credits and GPA meet the thesis requirements."""
    return (credits >= 120 and gpa >= 2.0)

def missing(credits, gpa) -> list[str]:
    """Return human-readable reasons if credits or GPA are below requirements."""
    reasons = []
    if credits < 120:
        missing_credits = 120-credits
        credit_reason = f"need {missing_credits} more credits"
        reasons.append(credit_reason)
    if gpa < 2.0:
        missing_gpa = 2.0-gpa
        gpa_reason = f"need {missing_gpa:.1f} more gpa"
        reasons.append(gpa_reason)
    return reasons