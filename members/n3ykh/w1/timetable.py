def by_day(schedule: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Group course names by day and sort each day's courses."""
    timetable = {}
    for course, day in schedule:
        timetable.setdefault(day, []).append(course)
    for day, courses in timetable.items():
        courses.sort()
    return timetable
