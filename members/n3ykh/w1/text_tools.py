def word_count(text: str) -> dict[str, int]:
    clean_text = text.lower()
    for x in ".,!?;:":
        clean_text = clean_text.replace(x, "")
    words = clean_text.split()
    answer = {}
    for x in words:
        answer[x] = answer.get(x, 0) + 1
    return answer

def top_k(text: str, k: int) -> list[tuple[str, int]]:
    answer = word_count(text)
    sorted_items = sorted(answer.items(), key = lambda item: (-item[1], item[0]))
    return sorted_items[:k]