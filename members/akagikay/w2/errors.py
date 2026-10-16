from .models import Task


class InfeasiblePlan(Exception):
    def __init__(self, needed_h: float, available_h: float):
        self.needed_h = needed_h
        self.available_h = available_h
        Exception.__init__(self, self.__str__())

    def __str__(self):
        return f"Infeasible plan: Required {self.needed_h} hours, available hours: {self.available_h} hours"

def check_feasible(tasks: list[Task], available_h: float):
    if (needed := sum(t.effort_h for t in tasks)) > available_h:
        raise InfeasiblePlan(needed, available_h)