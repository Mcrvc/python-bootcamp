"""Custom exceptions and validation for plan feasibility."""

from .models import Task


class InfeasiblePlan(Exception):
    """Exception raised when required study hours exceed available hours."""

    def __init__(self, needed_h: float, available_h: float) -> None:
        """Initialize exception with required and available hours."""
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(f"Can {needed_h}h nhung chi co {available_h}h")

    def __str__(self) -> str:
        """Return formatted error message."""
        return f"InfeasiblePlan: needed {self.needed_h}h, available {self.available_h}h"


def check_feasible(tasks: list[Task], available_h: float) -> None:
    """Verify total required effort does not exceed available hours."""
    totalNeededHours = 0.0
    for taskItem in tasks:
        totalNeededHours += taskItem.effort_h

    if totalNeededHours > available_h:
        raise InfeasiblePlan(needed_h=totalNeededHours, available_h=available_h)