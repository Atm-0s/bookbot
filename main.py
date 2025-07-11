import sys

from stats import get_word_count

from stats import get_character_count

from stats import sort_dict

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else: book_path = sys.argv[1]

def get_book_text(book_text):
    with open(book_text) as book:
        book_contents = book.read()
        return book_contents


book_text = get_book_text(book_path)
word_count = get_word_count(book_path)
char_counts = get_character_count(book_path)
sorted_chars = sort_dict(char_counts)


def report(book_path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for i in sorted_chars:
        n = sorted_chars[i]
        print(f"{i}: {n}")
    print("============= END ===============")


def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for i in sorted_chars:
       print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")
    

main()