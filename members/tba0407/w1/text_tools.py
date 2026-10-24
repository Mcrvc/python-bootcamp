def word_count(text: str) -> dict[str, int]:
    """Count lowercase words after removing basic punctuation."""
    text = text.lower()

    for punc in ".,!?;:":
        text = text.replace(punc, "")

    words = text.split()

    counts: dict[str, int] = {}

    for word in words:
        counts[word] = counts.get(word, 0) + 1

    return counts


def _sort_key(item: tuple[str, int]) -> tuple[int, str]:
    """Sort word counts by descending count and then alphabetically."""
    return (-item[1], item[0])


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    """Return the ``k`` most frequent words in deterministic order."""
    counts = word_count(text)
    sorted_counts = sorted(counts.items(), key=_sort_key)
    return sorted_counts[:k]
