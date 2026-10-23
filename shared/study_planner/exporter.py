
"""Export generated study plans as Markdown or plain-text reports."""

from collections.abc import Sequence
from pathlib import Path

from shared.contract import Block
from shared.study_planner.render import render


def render_markdown(blocks: Sequence[Block]) -> str:
    """Return a study plan formatted as Markdown.

    Args:
        blocks: The allocated study-plan blocks.

    Returns:
        A Markdown document describing the scheduled tasks.
    """
    if not blocks:
        return "# Study Plan\n\nNo tasks scheduled.\n"

    total_hours = sum(block.hours for block in blocks)
    lines = [
        "# Study Plan",
        "",
        f"**Total allocated time:** {total_hours:.1f} hours",
        "",
        "## Scheduled tasks",
        "",
    ]

    for number, block in enumerate(blocks, start=1):
        lines.extend(
            [
                f"### {number}. {block.task.title}",
                f"- **Hours:** {block.hours:.1f}",
                f"- **Importance:** {block.task.importance}/5",
                f"- **Deadline:** {block.task.deadline.isoformat()}",
                "",
            ]
        )

    return "\n".join(lines)


def export_markdown(
    blocks: Sequence[Block], path: str | Path
) -> None:
    """Write a study plan to a Markdown file.

    Args:
        blocks: The allocated study-plan blocks.
        path: Destination path for the Markdown file.

    Raises:
        OSError: If the destination cannot be written.
    """
    output = Path(path)
    output.write_text(render_markdown(blocks), encoding="utf-8")


def export_text(
    blocks: Sequence[Block], path: str | Path
) -> None:
    """Write a study plan as a plain-text report.

    Args:
        blocks: The allocated study-plan blocks.
        path: Destination path for the text report.

    Raises:
        OSError: If the destination cannot be written.
    """
    output = Path(path)
    output.write_text(render(list(blocks)) + "\n", encoding="utf-8")
