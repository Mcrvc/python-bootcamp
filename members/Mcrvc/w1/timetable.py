"""Timetable grouping by day."""

def by_day(pairs: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Group course/day pairs into a day -> sorted courses mapping."""
    group: dict[str, list[str]] = {}
    for course, day in pairs:
        group.setdefault(day, []).append(course)
    for crs in group.values():
        crs.sort()
    return group
