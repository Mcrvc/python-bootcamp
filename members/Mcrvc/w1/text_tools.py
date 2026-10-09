def word_count(text: str) -> dict[str, int]:
    count = {}
    for ch in ".,!?;:":
        text = text.replace(ch, "")
    words = text.lower().split()
    for word in words:
        if word in count:
            count[word] = count[word] + 1
        else:
            count[word] = 1
    return count


def getFreq(item):
    return item[1]  

def top_k(text: str, k: int) -> list[tuple[str, int]]:
    if k <= 0:
        return []
    count = word_count(text)
    res = list(count.items())
    res.sort()                 
    res.sort(key=getFreq, reverse=True)
    return res[:k]
