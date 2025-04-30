import sys
from stats import get_num_words, get_num_characters, format_dict

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def print_book_report(path, wordnum, list):
    print("============ BOOKBOT ============")
    print(f"Analysing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {wordnum} total words")
    print("--------- Character Count -------")
    for i in list:
        if not i["char"].isalpha():
            continue
        print(f"{i['char']}: {i['num']}")
    print("============= END ===============")

def main():
    # book_path = "books/frankenstein.txt"
    if (len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        book_text = get_book_text(book_path)
        num_words = get_num_words(book_text)
        characters = get_num_characters(book_text)
        list_chars = format_dict(characters)

        print_book_report(book_path, num_words, list_chars)   

main()
