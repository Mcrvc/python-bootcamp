def by_day(schedule: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Group course names by day and sort each day's courses."""
    result: dict[str, list[str]] = {}

    for course, day in schedule:
        result.setdefault(day, []).append(course)

    for courses in result.values():
        courses.sort()

    return result
