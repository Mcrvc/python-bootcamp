from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    """A study task with title, importance, effort hours and deadline."""

    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self) -> None:
        """Validate that importance is in 1..5."""
        if not 1 <= self.importance <= 5:
            raise ValueError("importance must be 1-5")

    def days_left(self, today: date) -> int:
        """Return days until deadline, clamped at 0 for overdue tasks."""
        delta = (self.deadline - today).days
        return max(0, delta)
