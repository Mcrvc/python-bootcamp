from .models import Task


class InfeasiblePlan(Exception):
    """Raised when tasks need more time than is available."""

    def __init__(self, needed_h: float, available_h: float) -> None:
        """Store the required and available study hours."""
        super().__init__(needed_h, available_h)
        self.needed_h = needed_h
        self.available_h = available_h

    def __str__(self) -> str:
        """Return a readable explanation of the infeasible plan."""
        return (
            f"Plan needs {self.needed_h} hours, "
            f"but only {self.available_h} hours are available"
        )


def check_feasible(tasks: list[Task], available_h: float) -> None:
    """Raise ``InfeasiblePlan`` if task effort exceeds available hours."""
    needed_h = sum(task.effort_h for task in tasks)

    if needed_h > available_h:
        raise InfeasiblePlan(needed_h, available_h)
