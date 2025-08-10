from stats import get_num_words
from stats import count_characters
from stats import sort_dict

word_count = get_num_words()
characters = count_characters()
list_dict = sort_dict(characters)
print(f"""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
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
