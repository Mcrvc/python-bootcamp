
from pathlib import Path
import sys


class StudyPlannerError(Exception):
    pass


class InfeasiblePlan(StudyPlannerError):

    def __init__(self, needed_h: float, available_h: float):
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(f"need {needed_h} hours but only {available_h} available")


class MissingFileError(StudyPlannerError, FileNotFoundError):
    pass


class EmptyFileError(StudyPlannerError, ValueError):
    pass


def validate_file(path: str | Path) -> Path:
  
    file_path = Path(path)
    if not file_path.exists() or not file_path.is_file():
        raise MissingFileError(f"Tasks file not found: {file_path}")

    if file_path.stat().st_size == 0:
        raise EmptyFileError(f"Tasks file is empty: {file_path}")

    return file_path


def check_feasible(needed_h: float, available_h: float) -> None:
   
    if needed_h > available_h:
        raise InfeasiblePlan(needed_h, available_h)


def handle_exception(exc: Exception) -> int:

    if isinstance(exc, MissingFileError):
        sys.stderr.write(f"Error: {exc}\n")
        return 1
    if isinstance(exc, EmptyFileError):
        sys.stderr.write(f"Error: {exc}\n")
        return 1
    if isinstance(exc, InfeasiblePlan):
        sys.stderr.write(f"Error: Infeasible plan - {exc}\n")
        return 2
    if isinstance(exc, StudyPlannerError):
        sys.stderr.write(f"Error: {exc}\n")
        return 1

    sys.stderr.write(f"Unexpected error: {exc}\n")
    return 1