"""Custom exceptions for the study planner."""

class InfeasiblePlan(Exception):
    """Exception raised when the total task effort exceeds available hours."""
    def __init__(self, needed_h, available_h):
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(
            f"plan needs {needed_h} h but only {available_h} h available"
        )

def check_feasible(tasks, available_h):
    """Check if the total effort of tasks is feasible within available hours."""
    needed = sum(t.effort_h for t in tasks)
    if needed > available_h:
        raise InfeasiblePlan(needed, available_h)