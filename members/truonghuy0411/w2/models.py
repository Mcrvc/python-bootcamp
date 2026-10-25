"""Task data model and date calculations."""

from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    """A study task with title, importance, estimated effort, and deadline."""

    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self) -> None:
        """Validate task attributes."""
        if self.importance < 1 or self.importance > 5:
            raise ValueError("importance must be 1-5")

    def days_left(self, today: date) -> int:
        """Calculate remaining days until deadline from today (minimum 0)."""
        remainingDays = (self.deadline - today).days
        if remainingDays < 0:
            return 0
        return remainingDays