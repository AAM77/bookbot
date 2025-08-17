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

def get_character_dictionaries_list(character_counts: dict) -> list:
    return [{"name": character, "num": count} for character, count in character_counts.items()]

def sort_on(items):
    return items["num"]

def get_sorted_dictionaries(character_counts: dict) -> list:
    char_dictionaries_list: list = get_character_dictionaries_list(character_counts)
    char_dictionaries_list.sort(reverse=True, key=sort_on)
    return char_dictionaries_list
