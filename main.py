from stats import get_num_words
from stats import count_characters

word_count = get_num_words()
characters = count_characters()
print(f"{word_count} words found in the document")
for char in characters:
    count = characters[char]
    print(f"'{char}': {count}")
