def can_register_thesis(credits: int, gpa: float) -> bool:
    return credits >= 120 and gpa >= 2.0


def missing(credits: int, gpa: float) -> list[str]:
    reason = []
    if credits < 120:
        needCre = 120 - credits
        reason.append(f"need {needCre} more credits")
    if gpa < 2.0:
        needGpa = round(2.0 - gpa, 2)
        reason.append(f"need {needGpa} more GPA")
    return reason
