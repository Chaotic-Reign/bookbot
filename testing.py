from stats import count_characters
from stats import sort_on

def sort_dict(chars_dict):
    chars_list = []
    for char, count in chars_dict.items():
        char_dict = {"char": char, "count": count}
        chars_list.append(char_dict)
    chars_list.sort(reverse=True, key=sort_on)
    print(chars_list)

characters = count_characters()
chars_list = sort_dict(characters)