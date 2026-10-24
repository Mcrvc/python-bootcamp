"""Log statistics: counts, slowest name, and p95 latency per name."""


from math import ceil


def analyse(pairs: list[tuple[str, float]]) -> dict:
    """Compute per-name request statistics from (name, latency) pairs.

    Args:
        pairs: List of (name, latency_ms) tuples.

    Returns:
        A dict with "counts", "slowest", and "p95" keys.

    """
    counts: dict[str, int] = {}
    times_by_name: dict[str, list[float]] = {}

    for name, time in pairs:
        counts[name] = counts.get(name, 0) + 1
        times_by_name.setdefault(name, []).append(time)

    p95: dict[str, float] = {}
    for name, times in times_by_name.items():
        sorted_times = sorted(times)
        n = len(sorted_times)
        rank = ceil(0.95 * n)
        idx = max(0, min(rank - 1, n - 1))
        p95[name] = sorted_times[idx]

    slowest = max(p95, key=p95.get)

    return {"counts": counts, "slowest": slowest, "p95": p95}
