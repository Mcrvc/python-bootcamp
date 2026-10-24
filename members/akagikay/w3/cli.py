import argparse
import sys
from collections.abc import Sequence
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from ..w2.io_utils import load_tasks
from ..w2.models import Task


@dataclass
class Block:
    """A task scheduled into a number of hours tonight."""

    task: Task
    hours: float


def _priority(task: Task, today: date) -> float:
    """Return the priority score: importance per day left until the deadline."""
    return task.importance / max(1, task.days_left(today))


def build_blocks(tasks: Sequence[Task], today: date, hours: float) -> list[Block]:
    """Fill ``hours`` with tasks, highest priority first.

    Overdue tasks (deadline before ``today``) are skipped. The last task
    may be scheduled partially when the remaining hours are smaller than
    its effort.

    Args:
        tasks: Candidate tasks, any order.
        today: Reference date used for prioritisation.
        hours: Hours available tonight.

    Returns:
        The scheduled blocks.

    Raises:
        ValueError: If ``hours`` is negative.
    """
    if hours < 0:
        raise ValueError("hours must be >= 0")

    ordered = sorted(tasks, key=lambda t: _priority(t, today), reverse=True)
    blocks: list[Block] = []
    remaining = float(hours)
    for task in ordered:
        if task.deadline < today:
            continue
        if remaining <= 0:
            break
        chunk = min(task.effort_h, remaining)
        if chunk <= 0:
            continue
        blocks.append(Block(task=task, hours=chunk))
        remaining -= chunk
    return blocks


def format_plan(blocks: Sequence[Block]) -> str:
    """Render blocks as the ``Tonight (...)`` plan with dotted leaders."""
    if not blocks:
        return "No tasks scheduled."

    total = sum(block.hours for block in blocks)
    width = max(len(block.task.title) for block in blocks) + 7
    lines = [f"Tonight ({total:.1f} h):"]
    for number, block in enumerate(blocks, start=1):
        name = f"{block.task.title} ".ljust(width, ".")
        lines.append(f" {number}. {name} {block.hours:.1f} h")
    return "\n".join(lines)


def _parse_date(text: str) -> date:
    """Convert an ISO date from the command line or fail with a clear message."""
    try:
        return date.fromisoformat(text)
    except ValueError:
        raise argparse.ArgumentTypeError(
            f"invalid date {text!r}, expected YYYY-MM-DD"
        ) from None


def main(argv: Sequence[str] | None = None) -> int:
    """Run the command-line study planner.

    Args:
        argv: Command-line arguments; defaults to ``sys.argv[1:]``.

    Returns:
        The exit code: 0 on success, 1 on bad input (e.g. a missing file).
    """
    parser = argparse.ArgumentParser(
        prog="python -m members.akagikay.w3.cli",
        description="Print a study plan for tonight from a task CSV file.",
    )
    parser.add_argument(
        "file",
        type=Path,
        help="CSV file with the columns title, importance, effort_h, deadline",
    )
    parser.add_argument(
        "--hours",
        type=float,
        required=True,
        help="hours available tonight",
    )
    parser.add_argument(
        "--today",
        type=_parse_date,
        default=None,
        help="reference date YYYY-MM-DD (default: today)",
    )
    args = parser.parse_args(argv)

    path: Path = args.file
    if not path.exists():
        print(f"File not found: {path}", file=sys.stderr)
        return 1

    try:
        tasks = load_tasks(path)
    except (OSError, ValueError) as error:
        print(f"Could not read {path}: {error}", file=sys.stderr)
        return 1

    today = args.today if args.today is not None else date.today()
    try:
        blocks = build_blocks(tasks, today, args.hours)
    except ValueError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    print(format_plan(blocks))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
