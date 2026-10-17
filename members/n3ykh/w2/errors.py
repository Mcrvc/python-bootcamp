from __future__ import annotations

try:
    from .models import Task
except ImportError:
    from models import Task

class InfeasiblePlan(Exception):
    """Exception raised when total required effort exceeds available hours."""

    def __init__(self, needed_h: float, available_h: float) -> None:
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(str(self))

    def __str__(self) -> str:
        return (
            f"Infeasible plan: needed {self.needed_h}h, "
            f"but only {self.available_h}h available."
        )

def check_feasible(tasks: list[Task], available_h: float) -> bool:
    """Verify if all tasks can be completed within available_h; raise InfeasiblePlan otherwise."""
    needed_h = sum(task.effort_h for task in tasks)
    if needed_h > available_h:
        raise InfeasiblePlan(needed_h, available_h)
    return True