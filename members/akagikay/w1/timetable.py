def by_day(schedule: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Group course codes by weekday, sorted within each day."""
    result = {}
    for course, day in schedule:
        result.setdefault(day, []).append(course)
    for day in result:
        result[day].sort()
    return result