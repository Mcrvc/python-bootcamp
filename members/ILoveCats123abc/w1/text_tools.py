"""Word counter and top-k words with highest frequency."""

from collections import Counter

PUNCT = str.maketrans("","",".,!?;:")

def word_count(text: str) -> dict[str, int]:
    """Count word frequency within text, ignoring punctuation and case."""
    cleaned = text.lower().translate(PUNCT)
    words = cleaned.split()
    return dict(Counter(words))

def top_k(text: str, k: int) -> list[tuple[str, int]]:
    """Return top-k words sorted by frequency and alphabetically."""
    counts = word_count(text)
    ordered = sorted(counts.items(), key = lambda pair: (-pair[1], pair[0]))
    return ordered[:k]