from shared.contract import Block


def render(blocks: list[Block]) -> str:
    """Return a readable study plan."""
    if not blocks:
        return "No tasks scheduled."

    for block in blocks:
        if block.hours < 0:
            raise ValueError("block hours must be non-negative")

    total_hours = sum(block.hours for block in blocks)
    lines = [f"Tonight ({total_hours:.1f} h):"]

    for number, block in enumerate(blocks, start=1):
        lines.append(f"{number}. {block.task.title}: {block.hours:.1f} h")

    return "\n".join(lines)
