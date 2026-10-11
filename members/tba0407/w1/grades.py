def summary(scores: list[float]) -> dict:
    n = len(scores)
    if n == 0:
        raise ValueError("List is empty")

    minVal = min(scores)
    maxVal = max(scores)


    meanVal = round(sum(scores) / n, 2)

    sortedScores = sorted(scores)


    mid = n // 2
    if n % 2 == 0:
        median = round((sortedScores[mid - 1] + sortedScores[mid]) / 2, 2)
    else:
        median = round(sortedScores[mid],2)


    return {
        "min": minVal,
        "max": maxVal,
        "mean": meanVal,
        "median": median
    }