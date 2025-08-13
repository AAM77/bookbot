from stats import count_num_words

def main() -> None:
    book_text = get_book_text("books/frankenstein.txt")
    word_count = count_num_words(book_text)
    print(f"{word_count} words found in the document")

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

main()