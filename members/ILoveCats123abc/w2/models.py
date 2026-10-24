"""Task model for the study planner."""

from dataclasses import dataclass
from datetime import date


@dataclass 
class Task:
    """Represent a task with title, importance, effort and deadline."""
    title: str 
    importance: int 
    effort_h: float
    deadline: date
  
    def __post_init__(self):
        """Validate that importance is within valid range of 1 to 5."""
        if not 1 <= self.importance <= 5:
            raise ValueError("importance must be 1-5")

    def days_left(self, today: date) -> int:
        """Calculate the remaining days before the deadline of the task."""
        return max((self.deadline-today).days,0)