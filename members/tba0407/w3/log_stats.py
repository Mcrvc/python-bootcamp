"""Summarise request counts and latency values from chat logs."""

from collections import Counter, defaultdict
from math import ceil
from typing import TypedDict


class LogStats(TypedDict):
    """Summary values returned by :func:`analyse`."""

    counts: dict[str, int]
    p95: dict[str, int]
    slowest: str | None


def analyse(pairs: list[tuple[str, int]]) -> LogStats:
    """Return request counts, nearest-rank p95 values, and slowest route."""
    counts = Counter(route for route, _ in pairs)
    latencies: defaultdict[str, list[int]] = defaultdict(list)

    for route, latency_ms in pairs:
        latencies[route].append(latency_ms)

    p95 = {}
    for route, values in latencies.items():
        ordered = sorted(values)
        index = ceil(0.95 * len(ordered)) - 1
        p95[route] = ordered[index]

    slowest = max(p95, key=p95.get) if p95 else None
    return {"counts": dict(counts), "p95": p95, "slowest": slowest}
