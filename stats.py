def get_word_count(book_text):
    with open(book_text) as book:
        book_contents = book.read()
        words_list = book_contents.split()
        return len(words_list)