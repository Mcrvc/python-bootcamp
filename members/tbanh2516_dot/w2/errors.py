"""w2-3: custom exceptions"""

from .models import Task


class InfeasiblePlan(Exception):
    """Raised when tasks need more hours than are available."""

    def __init__(self, needed_h: float, available_h: float) -> None:
        """Initialize InfeasiblePlan."""
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(needed_h, available_h)

    def __str__(self) -> str:
        """Return a string representation of InfeasiblePlan."""
        return f"Needed {self.needed_h} hours, but only {self.available_h} hours are available."


def check_feasible(tasks: list[Task], available_h: float) -> None:
    """Raise InfeasiblePlan if the total effort is more than the available hours."""
    total_needed_h = sum(t.effort_h for t in tasks)
    if total_needed_h > available_h:
        raise InfeasiblePlan(total_needed_h, available_h)
