def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def get_num_words():
    words = get_book_text("books/frankenstein.txt")
    words = words.split()
    return len(words)

def count_characters():
    text = get_book_text("books/frankenstein.txt")
    text = text.lower()
    characters = {}
    for char in text:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

