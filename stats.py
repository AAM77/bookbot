def count_num_words(file_contents: str) -> int:
    word_list: list = file_contents.split()
    word_count: int = len(word_list)
    return word_count