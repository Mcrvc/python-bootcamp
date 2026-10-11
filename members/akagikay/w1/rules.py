def can_register_thesis(credits: int, gpa: float) -> bool:
    return credits >= 120 and gpa >= 2.0

def missing(credits: int, gpa: float) -> list[str]:
    reasons = []
    if credits < 120:
        diffc = 120 - credits
        reasons.append(f"need {diffc} more credits")
    if gpa < 2.0:
        diffgpa = round(2.0 - gpa, 2)
        reasons.append(f"need {diffgpa} more GPA")
    return reasons