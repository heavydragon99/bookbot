from stats import get_num_words, get_num_characters, sort_dict
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_file = sys.argv[1]
    book_text = get_book_text(path_to_file)
    num_words = get_num_words(book_text)
    num_characters = get_num_characters(book_text)
    sorted_characters = sort_dict(num_characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("---------- Character Count -------")
    for char_info in sorted_characters:
        if char_info["char"].isalpha():
            print(f"{char_info['char']}: {char_info['num']}")
    print("============= END ===============")

main()

