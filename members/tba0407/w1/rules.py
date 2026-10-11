def can_register_thesis(credits: int, gpa: float) -> bool:
    return credits >= 120 and gpa >= 2.0

def missing(credits: int, gpa: float) -> list[str]:
    result = []
    
    if credits < 120:
        needed = 120 - credits
        result.append(f"need {needed} more credits")
        
    if gpa < 2.0:
        neededGpa = 2 - gpa
        result.append(f"need {neededGpa:.2f} more GPA")
        
    return result