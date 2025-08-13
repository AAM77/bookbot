def main():
    print(get_book_text("books/frankenstein.txt"))

def get_book_text(filepath: str):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

main()