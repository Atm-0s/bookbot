def get_book_text(book_text):
    with open(book_text) as book:
        book_contents = book.read()
        return book_contents

def main():
    print(get_book_text('./books/frankenstein.txt'))

main()

