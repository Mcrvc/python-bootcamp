def summary(scores: list[float]) -> dict[str, float]:
    """Return the minimum, maximum, mean, and median score."""
    n = len(scores)
    if n == 0:
        raise ValueError("List is empty")

    minimum = min(scores)
    maximum = max(scores)
    mean = round(sum(scores) / n, 2)
    sorted_scores = sorted(scores)
    mid = n // 2

    if n % 2 == 0:
        median = round((sorted_scores[mid - 1] + sorted_scores[mid]) / 2, 2)
    else:
        median = round(sorted_scores[mid], 2)

    return {
        "min": minimum,
        "max": maximum,
        "mean": mean,
        "median": median,
    }
