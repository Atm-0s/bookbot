def get_book_text(book_text):
    with open(book_text) as book:
        book_contents = book.read()
        return book_contents

def get_word_count(book_text):
    with open(book_text) as book:
        book_contents = book.read()
        words_list = book_contents.split()
        return len(words_list)

def main():
    print(f'{get_word_count('./books/frankenstein.txt')} words found in the document')

main()