from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    """A study task with importance, effort, and a deadline."""

    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self) -> None:
        """Validate the task's importance rating."""
        if not 1 <= self.importance <= 5:
            raise ValueError("importance must be between 1 and 5")

    def days_left(self, today: date) -> int:
        """Return non-negative whole days until the deadline."""
        return max((self.deadline - today).days, 0)
