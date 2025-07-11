def get_word_count(book_text):
    with open(book_text) as book:
        book_contents = book.read()
        words_list = book_contents.split()
        return len(words_list)
    
def get_character_count(book_path):
    
    letter_dict = {}
               
    with open(book_path) as book:
        book_contents = book.read()
        lowered_case = book_contents.lower()
        
        
        for i in lowered_case:
            if i not in letter_dict:
                letter_dict[i] = 1
            else: letter_dict[i] += 1
            
    return letter_dict

def sort_dict(character_dictionary):
    dict_list = []
    for character in character_dictionary:
        num = character_dictionary[character]
        if character.isalpha() == True:
            dict_list.append({"char": character, "num": num})
    
    dict_list.sort(reverse=True, key=lambda item: item["num"])



    return dict_list




    
   


