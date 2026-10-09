def word_count(text: str) -> dict[str, int]:
    text = text.lower()

    for punc in ".,!?;:":
        text = text.replace(punc, "")

    words = text.split()

    counts = {}

    for word in words:
        counts[word] = counts.get(word, 0) + 1

    return counts


def sortKey(item : tuple[str, int]) -> tuple[int, str]:
    return (-item[1], item[0])

def top_k(text: str, k: int) -> list[tuple[str, int]]:

    counts = word_count(text)

    sortedList = sorted(counts.items(), key = sortKey)

    return sortedList[:k]

