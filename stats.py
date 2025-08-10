def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def get_num_words(text):
    text = text.split()
    return len(text)

def count_characters(text):
    text = text.lower()
    characters = {}
    for char in text:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

def sort_on(items):
    return items["count"]

def sort_dict(chars_dict):
    chars_list = []
    for char, count in chars_dict.items():
        char_dict = {"char": char, "count": count}
        chars_list.append(char_dict)
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list
