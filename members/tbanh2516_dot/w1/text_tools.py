PUNCTUATION = ".,!?;:"

def word_count(text: str) -> dict[str, int]:
    text = text.lower()
    for ch in PUNCTUATION:
        text = text.replace(ch, "")
    counts: dict[str, int] = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    pairs = word_count(text).items()
    ordered_pairs = sorted(pairs, key=lambda x: (-x[1], x[0]))
    return ordered_pairs[:k]