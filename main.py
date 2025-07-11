def get_book_text(book_text):
    with open(book_text) as book:
        book_contents = book.read()
        return book_contents

from stats import get_word_count

def main():
    print(f'{get_word_count('./books/frankenstein.txt')} words found in the document')

main()