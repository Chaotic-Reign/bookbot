import sys
from stats import get_num_words
from stats import count_characters
from stats import sort_dict
from stats import get_book_text


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    text = get_book_text(book_path)
    word_count = get_num_words(text)
    characters = count_characters(text)
    list_dict = sort_dict(characters)
    print(f"""============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------
    """)
    for char_dict in list_dict:
        if char_dict["char"].isalpha():
            char = char_dict["char"]
            count = char_dict["count"]
            print(f"{char}: {count}")
    print("============= END ===============")

main()