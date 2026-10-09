def can_register_thesis(credits: int, gpa: float) -> bool:
    return credits >= 120 and gpa >= 2.0

def missing(credits: int, gpa: float) -> list[str]:
    result = []
    
    if credits < 120:
        result.append("Needs more credits")
    if gpa < 2.0:
        result.append("GPA too low")
        
    return result