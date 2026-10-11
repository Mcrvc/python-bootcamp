def summary(scores: list[float]) -> dict:
    if not scores:
        raise ValueError("Empty list")

    sort = sorted(scores)
    n = len(sort)
    mid = n // 2
    if n % 2 == 1:
        median = sort[mid]
    else:
        median = (sort[mid - 1] + sort[mid]) / 2

    return {
        "min": sort[0],
        "max": sort[-1],
        "mean": round(sum(scores) / n, 2),
        "median": round(median, 2),
    }
