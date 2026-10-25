"""Text processing and word frequency tools."""


def word_count(text: str) -> dict[str, int]:
    """Count occurrences of each word in text, ignoring punctuation and case."""
    for char in ".,!?;:":
        text = text.replace(char, " ")

    counts: dict[str, int] = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    """Return the top k most frequent words sorted by count, then alphabetically."""
    counts = word_count(text)
    return sorted(counts.items(), key=lambda x: (-x[1], x[0]))[:k]

