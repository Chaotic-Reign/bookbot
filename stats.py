def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def get_num_words(path_to_file):
    result = get_book_text(path_to_file)
    words = result.split()
    num_words = 0
    for word in words:
        num_words += 1
    print(f"{num_words} words found in the document")

def count_characters(path_to_file):
    text = get_book_text(path_to_file)
    text = text.lower()
    words = text.split()
    characters = {}
    for word in words:
        for char in word:
            if f"{char}" in characters:
                char += 1
            else:
                characters[{char}] = 1
    return characters

