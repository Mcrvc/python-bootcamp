"""Log statistics and latency analysis."""

from __future__ import annotations

import math
from collections import Counter, defaultdict
from typing import Any


def analyse(pairs: list[tuple[str, float | int]]) -> dict[str, Any]:
    """Analyze request route latency pairs and compute p95 percentiles."""
    if not pairs:
        return {
            "counts": Counter(),
            "p95": {},
            "slowest": None,
        }

    counts: Counter[str] = Counter()
    latencies_by_route: dict[str, list[float]] = defaultdict(list)

    for route, latency in pairs:
        counts[route] += 1
        latencies_by_route[route].append(float(latency))

    p95_by_route: dict[str, float] = {}
    for route, latencies in latencies_by_route.items():
        sorted_latencies = sorted(latencies)
        rank_index = max(0, math.ceil(0.95 * len(sorted_latencies)) - 1)
        p95_by_route[route] = sorted_latencies[rank_index]

    slowest_route = max(
        p95_by_route,
        key=lambda route: (p95_by_route[route], counts[route]),
    )

    return {
        "counts": counts,
        "p95": p95_by_route,
        "slowest": slowest_route,
    }