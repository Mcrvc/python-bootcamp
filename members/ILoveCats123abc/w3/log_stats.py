"""Analyze chat log stats for the study planner."""

import math
from collections import Counter, defaultdict


def analyse(pairs: list[tuple[str, float]]) -> dict[str, object]:
    """Analyze request counts, P95 latency per route, and find the slowest route."""
    if not pairs:
        return {
            "counts": Counter(),
            "p95": {},
            "slowest": None
        }

    counts = Counter(route for route, _ in pairs)

    grouped_latencies = defaultdict(list)
    for route, latency in pairs:
        grouped_latencies[route].append(latency)

    p95_dict = {}
    for route, latencies in grouped_latencies.items():
        if not latencies:
            p95_dict[route] = 0.0
            continue
        
        sorted_lat = sorted(latencies)
        n = len(sorted_lat)
        idx = math.ceil(0.95 * n) - 1
        idx = max(0, min(idx, n - 1))
        p95_dict[route] = float(sorted_lat[idx])

    slowest_route = max(p95_dict, key=p95_dict.get) if p95_dict else None

    return {
        "counts": counts,
        "p95": p95_dict,
        "slowest": slowest_route
    }