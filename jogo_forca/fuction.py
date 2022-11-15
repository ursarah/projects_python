def find_all_indexes(word, value_to_find):
    indexes = []
    for index, letter in enumerate(word):
        if letter == value_to_find:
            indexes.append(index)            
    return indexes
   
def display_word(word):
    print(" ".join(word))

