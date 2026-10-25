def summary(scores: list[float]) -> dict[str, float]:
    """Return the minimum, maximum, mean, and median of the scores."""
    if len(scores) == 0:
        raise ValueError("List cannot be empty")

    mn = float("inf")
    mx = float("-inf")
    mean = 0
    cnt = 0
    for x in scores:
        mn = min(mn, x)
        mx = max(mx, x)
        mean += x
        cnt += 1
    mean /= cnt
    mean = round(mean, 2)

    sorted_scores = sorted(scores)
    mid = len(sorted_scores) // 2

    if len(sorted_scores) % 2 == 0:
        median = (sorted_scores[mid - 1] + sorted_scores[mid]) / 2
    else:
        median = sorted_scores[mid]

    median = round(median, 2)
    return {"min": mn, "max": mx, "mean": mean, "median": median}
