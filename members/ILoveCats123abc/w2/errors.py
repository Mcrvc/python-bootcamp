class InfeasiblePlan(Exception):
    def __init__(self, needed_h, available_h):
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(
            f"plan needs {needed_h} h but only {available_h} h available"
        )

def check_feasible(tasks, available_h):
    needed = sum(t.effort_h for t in tasks)
    if needed > available_h:
        raise InfeasiblePlan(needed, available_h)