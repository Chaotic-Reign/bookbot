from stats import get_num_words
from stats import count_characters

get_num_words("books/frankenstein.txt")

def get_character_counts():
    result = count_characters("books/frankenstein.txt")
    for value in result:
        count = result[value]
        print(f"character: {value}, count: {count}")