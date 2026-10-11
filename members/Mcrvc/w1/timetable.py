def by_day(pairs: list[tuple[str, str]]) -> dict[str, list[str]]:
    group = {}
    for course, day in pairs:
        group.setdefault(day, []).append(course)
    for crs in group.values():
        crs.sort()
    return group
