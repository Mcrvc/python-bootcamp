"""Log statistics: counts, slowest name, and p95 latency per name."""


from math import ceil


def analyse(pairs):
    counts = {}
    totals = {}
    times_by_name = {}

    for name, time in pairs:
        counts[name] = counts.get(name, 0) + 1
        totals[name] = totals.get(name, 0) + time
        times_by_name.setdefault(name, []).append(time)

    slowest = max(totals, key=totals.get)

    p95 = {}
    for name, times in times_by_name.items():
        sorted_times = sorted(times)
        n = len(sorted_times)
        rank = ceil(0.95 * n)
        idx = max(0, min(rank - 1, n - 1))
        p95[name] = sorted_times[idx]

    return {"counts": counts, "slowest": slowest, "p95": p95}
