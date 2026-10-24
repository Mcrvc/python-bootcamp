"""W3-2: statistics over (route, latency_ms) log pairs."""

import math
from collections import Counter, defaultdict


def _p95(values: list[float]) -> float:
    """Return the 95th percentile of values (nearest-rank method).

    Nearest-rank: sort the values, then take the element at 1-based rank
    ceil(0.95 * n). Example: [100, 200, 300] -> rank ceil(2.85) = 3 -> 300.

    Args:
        values: A non-empty list of latencies.

    Returns:
        The p95 latency.
    """
    ordered = sorted(values)
    rank = math.ceil(0.95 * len(ordered))
    return ordered[rank - 1]


def analyse(pairs: list[tuple[str, float]]) -> dict:
    """Summarise request logs per route.

    Args:
        pairs: (route, latency_ms) tuples, e.g. [("fee", 100), ("rag", 900)].

    Returns:
        A dict with three keys:
            "counts":  {route: number of requests}
            "p95":     {route: p95 latency}
            "slowest": the route with the highest p95 (None if pairs is empty)

    Example:
        >>> analyse([("fee", 100), ("rag", 900)])["slowest"]
        'rag'
    """
    counts = Counter(route for route, _ in pairs)
    by_route: defaultdict[str, list[float]] = defaultdict(list)
    for route, latency in pairs:
        by_route[route].append(latency)
    p95 = {route: _p95(latencies) for route, latencies in by_route.items()}
    if not p95:
        slowest = None
    else:
        slowest = max(p95, key=p95.get)
    return {"counts": dict(counts), "p95": p95, "slowest": slowest}
