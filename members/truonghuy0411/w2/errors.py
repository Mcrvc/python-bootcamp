from .models import Task


class InfeasiblePlan(Exception):
    def __init__(self, needed_h: float, available_h: float):
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(f"Can {needed_h}h nhung chi co {available_h}h")

    def __str__(self) -> str:
        return f"InfeasiblePlan: needed {self.needed_h}h, available {self.available_h}h"


def check_feasible(tasks: list[Task], available_h: float) -> None:
    totalNeededHours = 0.0
    for taskItem in tasks:
        totalNeededHours += taskItem.effort_h

    if totalNeededHours > available_h:
        raise InfeasiblePlan(needed_h=totalNeededHours, available_h=available_h)