def summary(scores: list[float]) -> dict:
    if not scores:
        raise ValueError("The scores list is empty.")
    ordered_scores = sorted(scores)
    n = len(ordered_scores)
    mid = n // 2
    if n % 2 == 0:
        median = (ordered_scores[mid - 1] + ordered_scores[mid]) / 2
    else:
        median = ordered_scores[mid]
    return {
        "min": min(ordered_scores),
        "max": max(ordered_scores),
        "mean": round(sum(ordered_scores) / n, 2),
        "median": round(median, 2)
    }