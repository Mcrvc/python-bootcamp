def summary(scores: list[float]) -> dict:
    if not scores:
        raise ValueError("scores list cannot be empty!")
    minVal = min(scores)
    maxVal = max(scores)

    meanVal = round(sum(scores) / len(scores), 2)

    sortedScores = sorted(scores)
    n = len(sortedScores)

    if n % 2 != 0:
        medianVal =  sortedScores[n // 2]
    else:
        mid1 = sortedScores[(n // 2) - 1]
        mid2 = sortedScores[(n // 2)]
        medianVal = (mid1 + mid2) / 2

    medianVal = round(medianVal, 2)

    return {
        "min": minVal,
        "max": maxVal,
        "mean": meanVal,
        "median": medianVal
    }