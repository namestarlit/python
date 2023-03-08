## RENAME THIS FILE FROM 27-ex25.py TO ex25.py TO USE IT ##

def break_words(stuff):
    """This function will break up words for us."""
    # split() function splits words
    words = stuff.split()
    return words

def sort_words(words):
    """Sorts the words."""
    # sorted() function sorts words
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    # pop() pops words, pop(0) pops one at index 0
    word = words.pop(0)
    print(word)
    return None

def print_last_word(words):
    """Prints the last word after popping it off."""
    # pop(-1) pops the last word at index -1
    word = words.pop(-1)
    print(word)
    return None

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    # break the sentence first using break_words()
    words = break_words(sentence)
    # return sorted words using sort_words()
    return sort_words(words)
def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    # break the words using break_word()
    words = break_words(sentence)
    # print the first word using print_first_word()
    print_first_word(words)
    # print the last word using print_last_word()
    print_last_word(words)
    return None

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    # sort the sentence using sort_sentence()
    words = sort_sentence(sentence)
    # print first word using print_first_word()
    print_first_word(words)
    # print last word using print_last_word()
    print_last_word(words)

    # I know it's over documentend :D
