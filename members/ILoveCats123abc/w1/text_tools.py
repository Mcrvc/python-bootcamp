from collections import Counter

PUNCT = str.maketrans("","",".,!?;:")

def word_count(text: str) -> dict[str, int]:
    cleaned = text.lower().translate(PUNCT)
    words = cleaned.split()
    return dict(Counter(words))

def top_k(text: str, k: int) -> list[tuple[str, int]]:
    counts = word_count(text)
    ordered = sorted(counts.items(), key = lambda pair: (-pair[1], pair[0]))
    return ordered[:k]