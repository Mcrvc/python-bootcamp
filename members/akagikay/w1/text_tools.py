def word_count(text: str) -> dict[str, int]:
    count = {}
    for chara in ".,!?;:":
        text = text.replace(chara, "")
    for word in text.lower().split():
        count[word] = count.get(word, 0) + 1
    return count


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    if k <= 0:
        return []
    count = word_count(text)
    res = list(count.items())
    res.sort(key=lambda item: item[0])
    res.sort(key=lambda item: item[1], reverse=True)
    return res[:k]