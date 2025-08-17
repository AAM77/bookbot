import sys

from stats import count_num_words
from stats import count_num_chars
from stats import get_sorted_dictionaries

def main() -> None:
    try:
        if len(sys.argv) == 2:
            text_path: str = sys.argv[1]
            book_text: str = get_book_text(text_path)
            word_count: int = count_num_words(book_text)
            character_counts: dict = count_num_chars(book_text)
            print(f"{word_count} words found in the document")
            print_report(text_path, word_count, character_counts)
        else:
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
    

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def print_report(text_path: str, word_count: int, character_counts: dict) -> None:
    sorted_character_dictionaries: list = get_sorted_dictionaries(character_counts)
    header_text: str = f"""
    ============ BOOKBOT ============
    Analyzing book found at {text_path}...
    ----------- Word Count ----------
    Found {word_count} total words
    --------- Character Count -------
    """
    ending_line: str = "============= END ==============="
    
    print(header_text)
    for character_dictionary in sorted_character_dictionaries:
        if character_dictionary["name"].isalpha():
            print(f"{character_dictionary["name"]}: {character_dictionary["num"]}")
    print(ending_line)
    


main()