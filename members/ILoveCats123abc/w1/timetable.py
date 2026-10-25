"""Group courses from timetable by weekdays."""

def by_day(pairs: list[tuple[str,str]]) -> dict[str, list[str]]:
    """Group courses from list of tuple by weekdays."""
    timetable = {}
    for course, day in pairs:
        timetable.setdefault(day, []).append(course)
    for day, courses in timetable.items():
        courses.sort()
    return timetable