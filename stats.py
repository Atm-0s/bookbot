def get_word_count(book_text):
    with open(book_text) as book:
        book_contents = book.read()
        words_list = book_contents.split()
        return len(words_list)
    
def get_character_count(book_text):
    
    letter_dict = {}
               
    with open(book_text) as book:
        book_contents = book.read()
        lowered_case = book_contents.lower()
        
        
        for i in lowered_case:
            if i not in letter_dict:
                letter_dict[i] = 1
            else: letter_dict[i] += 1
            
    return letter_dict

print(get_character_count('./books/frankenstein.txt'))
    


