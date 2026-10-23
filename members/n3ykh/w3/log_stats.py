"""Analyse route latency statistics."""

from collections import defaultdict
from math import ceil
from typing import TypedDict


class AnalysisResult(TypedDict):
    """Statistics calculated from route latency measurements."""

    counts: dict[str, int]
    p95: dict[str, int]
    slowest: str | None


def analyse(pairs: list[tuple[str, int]]) -> AnalysisResult:
    """Return route counts, p95 latencies, and the slowest route."""
    latencies: dict[str, list[int]] = defaultdict(list)

    for route, latency in pairs:
        latencies[route].append(latency)

    counts = {route: len(values) for route, values in latencies.items()}

    p95 = {}
    for route, values in latencies.items():
        values.sort()
        index = ceil(0.95 * len(values)) - 1
        p95[route] = values[index]

    slowest = max(p95, key=p95.get) if p95 else None

    return {
        "counts": counts,
        "p95": p95,
        "slowest": slowest,
    }
