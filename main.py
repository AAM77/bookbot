def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = count_num_words(book_text)
    print(f"{word_count} words found in the document")

def get_book_text(filepath: str):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def count_num_words(file_contents: str):
    word_list = file_contents.split()
    word_count = len(word_list)
    return word_count

main()