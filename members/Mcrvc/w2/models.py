"""Task model for the study planner."""

from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self) -> None:
        """Validate that the importance value is within the 1-5 range."""
        if not 1 <= self.importance <= 5:
            raise ValueError("importance must be 1-5")

    def days_left(self, today: date) -> int:
        """Return the number of days until the deadline, clamped to 0 if overdue."""
        left = (self.deadline - today).days
        if left < 0:
            return 0
        return left
