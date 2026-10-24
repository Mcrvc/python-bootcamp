"""Timetable grouping and sorting utilities."""


def by_day(timetable: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Group timetable courses by day and return them in sorted order."""
    result: dict[str, list[str]] = {}

    for course, day in timetable:
        result.setdefault(day, []).append(course)

    for courses in result.values():
        courses.sort()

    return result

