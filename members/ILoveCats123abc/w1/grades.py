def summary(scores: list[float]) -> dict:
    if not scores:
        raise ValueError("Empty score list")

    score_list = sorted(scores)
    min_score = score_list[0]
    max_score = score_list[-1]
    total_score = sum(score_list)
    length = len(score_list)
    mean = total_score/length

    if length%2 == 1:
        median = score_list[length//2]
    else:
        median = (score_list[length//2 - 1] + score_list[length//2])/2

    return {
        "min": min_score,
        "max": max_score,
        "mean": round(mean, 2),
        "median": round(median, 2)
    }