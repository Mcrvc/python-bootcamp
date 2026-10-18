class InfeasiblePlan(Exception):
    def __init__(self, needed_h: float, available_h: float):
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(f"need {needed_h} hours but only {available_h} available")


def check_feasible(tasks: list, available_h: float) -> None:
    needed_h = 0
    for t in tasks:
        needed_h = needed_h + t.effort_h
    if needed_h > available_h:
        raise InfeasiblePlan(needed_h, available_h)
