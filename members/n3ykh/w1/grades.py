def summary(scores: list[float]) -> dict:
    if len(scores) == 0:
        raise ValueError("List cannot be empty")  
    mn = float('inf')
    mx = float('-inf')
    mean = 0
    cnt = 0
    for x in scores:
        mn = min(mn, x)
        mx = max(mx, x)
        mean += x
        cnt += 1
    mean /= cnt
    mean = round(mean, 2)
    scores.sort()
    mid = len(scores) // 2
    if len(scores) % 2 == 0:
        median = (scores[mid - 1] + scores[mid]) / 2
    else:
        median = scores[mid] 
    median = round(median, 2)        
    return {'min': mn, 'max': mx, 'mean': mean, 'median': median}