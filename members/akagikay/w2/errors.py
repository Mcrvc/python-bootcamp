from .models import Task


class InfeasiblePlan(Exception):
    """Raised when required effort hours exceed available hours."""

    def __init__(self, needed_h: float, available_h: float):
        self.needed_h = needed_h
        self.available_h = available_h
        Exception.__init__(self, self.__str__())

    def __str__(self) -> str:
        return f"Infeasible plan: Required {self.needed_h} hours, available hours: {self.available_h} hours"


def check_feasible(tasks: list[Task], available_h: float) -> None:
    """Raise InfeasiblePlan if total effort exceeds available hours."""
    if (needed := sum(t.effort_h for t in tasks)) > available_h:
        raise InfeasiblePlan(needed, available_h)