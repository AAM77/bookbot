def count_num_words(file_contents: str) -> int:
    word_list: list = file_contents.split()
    word_count: int = len(word_list)
    return word_count

def count_num_chars(file_contents: str) -> dict:
    char_counts: dict[str, int] = {}
    lower_cased_contents: str = file_contents.lower()
    for char in lower_cased_contents:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts
    