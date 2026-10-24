"""Errors and feasibility checks for the study planner."""

from members.Mcrvc.w2.models import Task


class InfeasiblePlan(Exception):
    def __init__(self, needed_h: float, available_h: float) -> None:
        """Store the hours needed versus the hours available for a plan."""
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(f"need {needed_h} hours but only {available_h} available")


def check_feasible(tasks: list[Task], available_h: float) -> None:
    """Raise InfeasiblePlan when the total task effort exceeds the available hours."""
    needed_h = 0
    for t in tasks:
        needed_h = needed_h + t.effort_h
    if needed_h > available_h:
        raise InfeasiblePlan(needed_h, available_h)
