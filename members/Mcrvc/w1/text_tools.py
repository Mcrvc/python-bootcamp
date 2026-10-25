"""Word counting and top-k helpers."""

def word_count(text: str) -> dict[str, int]:
    """Count word frequencies in the text, ignoring punctuation and case."""
    count: dict[str, int] = {}
    for ch in ".,!?;:":
        text = text.replace(ch, "")
    words = text.lower().split()
    for word in words:
        if word in count:
            count[word] = count[word] + 1
        else:
            count[word] = 1
    return count


def getFreq(item: tuple[str, int]) -> int:
    """Return the frequency value used for sorting."""
    return item[1]

def top_k(text: str, k: int) -> list[tuple[str, int]]:
    """Return the top k words with their frequencies, sorted by frequency."""
    if k <= 0:
        return []
    count = word_count(text)
    res = list(count.items())
    res.sort()                 
    res.sort(key=getFreq, reverse=True)
    return res[:k]
