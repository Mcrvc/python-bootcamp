"""w1-2: word frequency counter and top-k extraction"""

PUNCTUATION = ".,!?;:"


def word_count(text: str) -> dict[str, int]:
    """Count word frequencies in a text, ignoring punctuation and case."""
    text = text.lower()
    for ch in PUNCTUATION:
        text = text.replace(ch, "")
    counts: dict[str, int] = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    """Return the k most frequent words in a text."""
    pairs = word_count(text).items()
    ordered_pairs = sorted(pairs, key=lambda x: (-x[1], x[0]))
    return ordered_pairs[:k]
