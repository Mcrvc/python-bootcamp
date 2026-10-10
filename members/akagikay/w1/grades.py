def summary(scores: list[float]) -> dict[str, float]:
    if not scores:
        raise ValueError("scores list cannot be empty")
    n = len(scores)
    sorteds = sorted(scores)
    mid = n // 2
    if n % 2 == 1:
        median = float(sorteds[mid])
    else:
        median = (sorteds[mid - 1] + sorteds[mid]) / 2
    median = round(median, 2)
    return {
        "min": min(scores),
        "max": max(scores),
        "mean": round(sum(scores) / n, 2),
        "median": median,
    }