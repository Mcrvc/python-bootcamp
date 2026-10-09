def missing(credits, gpa) -> list[str]:
    answer = []
    if credits < 120:
        dif_cre = 120 - credits
        answer.append(f"need {dif_cre} more credits")
    if gpa < 2.0:
        dif_gpa = 2.0 - gpa
        answer.append(f"need {dif_gpa} more gpa")
    return answer        

def can_register_thesis(credits: int, gpa: float) -> bool:
    return credits >= 120 and gpa >= 2.0