def by_day(pairs: list[tuple[str, str]]) -> dict[str, list[str]]:
    groups: dict[str, list[str]] = {}
    for course, day in pairs:
        groups.setdefault(day, []).append(course)
    return {k: sorted(v) for k, v in groups.items()}