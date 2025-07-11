def get_book_text(book_text):
    with open(book_text) as book:
        book_contents = book.read()
        return book_contents

from stats import get_word_count

from stats import get_character_count

def main():
    print(get_character_count('./books/frankenstein.txt'))

main()