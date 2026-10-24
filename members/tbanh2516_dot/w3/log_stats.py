"""W3-2 Chat log analysis: counts and p95 latency per route."""
import math
from collections import Counter, defaultdict


def p95(values: list[float]) -> float:
    """Return the 95th percentile (nearest-rank) of a non-empty list."""
    ordered = sorted(values)
    return ordered[math.ceil(0.95 * len(ordered)) - 1]


def analyse(pairs: list[tuple[str, float]]) -> dict:
    """Return request counts, p95 latency per route and the slowest route."""
    counts = Counter(route for route, _ in pairs)
    latencies: dict[str, list[float]] = defaultdict(list)
    for route, ms in pairs:
        latencies[route].append(ms)
    p95_by_route = {route: p95(values) for route, values in latencies.items()}
    if not p95_by_route:
        return {"counts": counts, "p95": p95_by_route, "slowest": None}
    slowest = max(p95_by_route, key=p95_by_route.get)
    return {"counts": counts, "p95": p95_by_route, "slowest": slowest}
