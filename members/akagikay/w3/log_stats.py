import math
from collections import Counter
from collections.abc import Sequence
from typing import TypedDict


class LogStats(TypedDict):
    counts: Counter[str]
    p95: dict[str, float]
    slowest: str | None


def p95(values: Sequence[float]) -> float:
    ordered = sorted(values)
    if not ordered:
        raise ValueError("values must not be empty")
    rank = math.ceil(0.95 * len(ordered))
    return ordered[rank - 1]


def analyse(pairs: Sequence[tuple[str, float]]) -> LogStats:
    counts: Counter[str] = Counter(route for route, _ in pairs)
    latencies: dict[str, list[float]] = {}
    for route, latency_ms in pairs:
        latencies.setdefault(route, []).append(latency_ms)

    percentiles = {route: p95(observed) for route, observed in latencies.items()}
    slowest = max(percentiles, key=percentiles.get, default=None)
    return {"counts": counts, "p95": percentiles, "slowest": slowest}
