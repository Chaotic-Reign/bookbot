def get_num_words():
    result = get_book_text("books/frankenstein.txt")
    words = result.split()
    num_words = 0
    for word in words:
        num_words += 1
    print(f"{num_words} words found in the document")