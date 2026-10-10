def by_day(pairs: list[tuple[str,str]]) -> dict:
    timetable = {}
    for course, day in pairs:
        timetable.setdefault(day, []).append(course)
    for day in timetable:
        timetable[day].sort()
    return timetable