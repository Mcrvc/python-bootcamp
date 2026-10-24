"""w1-5: timetable utilities"""


def by_day(pairs: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Group courses by day and sort them alphabetically."""
    groups: dict[str, list[str]] = {}
    for course, day in pairs:
        groups.setdefault(day, []).append(course)
    return {k: sorted(v) for k, v in groups.items()}
