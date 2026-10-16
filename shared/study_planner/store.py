"""Save generated study-plan blocks to a JSON file."""

import json
from dataclasses import asdict
from datetime import date
from pathlib import Path
from typing import Sequence

from shared.contract import Block


def _json_default(value: object) -> str:
    """Convert dates to ISO strings for JSON serialization."""
    if isinstance(value, date):
        return value.isoformat()

    raise TypeError(
        f"Object of type {type(value).__name__} is not JSON serializable"
    )


def save_json(blocks: Sequence[Block], path: str | Path) -> None:
    """Save schedule blocks as an indented JSON array.

    Each block contains its task fields and its allocated hours.
    Task deadlines are serialized as YYYY-MM-DD strings.

    Args:
        blocks: The schedule blocks to save.
        path: The destination JSON file path.

    Raises:
        OSError: If the destination cannot be written.
        TypeError: If the data contains an unsupported value.
    """
    output = Path(path)

    data = [asdict(block) for block in blocks]

    with output.open("w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            default=_json_default,
            indent=2,
            ensure_ascii=False,
        )
        file.write("\n")
