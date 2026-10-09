def can_register_thesis(credits: int, gpa: float) -> bool:
    return credits >= 120 and gpa >= 2.0

def missing(credits: int, gpa: float) -> list[str]:
    reasons = []
    
    if credits < 120:
        diff_credits = 120 - credits
        reasons.append(f"need {diff_credits} more credits")
        
    if gpa < 2.0:
        diff_gpa = round(2.0 - gpa, 2)
        reasons.append(f"need {diff_gpa} more gpa")
        
    return reasons
