from dataclasses import dataclass
from datetime import date

@dataclass
class Task: 
    """A study task with an importance from 1 to 5."""
    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self) -> None:
        if not (1 <= self.importance <= 5):
            raise ValueError("Importance must be between 1 and 5.")


    def days_left(self, today: date) -> int:
        """Return the number of days left until the deadline."""
        return max((self.deadline - today).days, 0)