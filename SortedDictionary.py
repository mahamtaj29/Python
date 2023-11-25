"""
Here I am implementing a simple dictionary to help a tourist while abroad.  The dictionary contains three useful words,
which are spanish translation of english words "hey, thanks, home". In addition I'll also implement the functions search word,
add word, remove word, print word and translate word using the dictionary.
"""
def text_conversion(english_spanish):
    """
    This function will convert the text string into spanish
    :return: str
    """
    enter_text = input("Enter the text to be translated into Spanish: ")
    empty_list = []
    empty_list = enter_text.split()
    print("The text, translated by the dictionary: ")
    for index in range(len(empty_list)):
        list_entity = empty_list[index]
        result = english_spanish.get(list_entity)
        # if word is not in Dict then print it as it is
        if result is None:
            result = list_entity
        print(result, end=" ")
    print()
def print_func(english_spanish):
    """
    This function will print the words in spanish and english as well
    """
    print()
    print("English-Spanish")
    for word in sorted(english_spanish):
        print(word, english_spanish[word])
    print()
    print("Spanish-English")
    spanish_english = dict([(value, key) for key, value in english_spanish.items()])
    for word in sorted(spanish_english):
        print(word, spanish_english[word])
    print()
def add_func(english_spanish):
    """
    This function will add the word in Dict
    """
    english_word = input("Give the word to be added in English: ")
    spanish_word = input("Give the word to be added in Spanish: ")
    # here new entity has been created to update in the dictionary
    new_entry = {english_word: spanish_word}
    english_spanish.update(new_entry)
def word_funct(english_spanish):
    """
    This function will give the word meaning in spanish
    """
    display_word = input("Enter the word to be translated: ")
    word = english_spanish.get(display_word)
    if word not in english_spanish.values():
        print("The word", display_word, "could not be found from the dictionary.")
    else:
        print(f"{display_word} in Spanish is {english_spanish[display_word]}")
def remove_fucntion(english_spanish):
    """
    This function will remove the word from dict.
    :param english_spanish: dict
    :return: updated dict, after removing the word
    """
    remove_word = input("Give the word to be removed: ")
    if remove_word in english_spanish.keys():
        del english_spanish[remove_word]
    else:
        print("The word", remove_word, "could not be found from the dictionary.")
def key_printing(english_spanish):
    """
    This function will print the contents of the Dict
    :param english_spanish dictionary
    """
    print("Dictionary contents:")
    dict_display = sorted(english_spanish.keys())
    print(", ".join(dict_display))

def main():
    english_spanish = {
        "hey": "hola",
        "thanks": "gracias",
        "home": "casa"
    }
    key_printing(english_spanish)
    while True:
        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")
        if command == "W":
            word_funct(english_spanish)
        elif command == "A":
            add_func(english_spanish)
            key_printing(english_spanish)
        elif command == "R":
            remove_fucntion(english_spanish)
        elif command == "P":
            print_func(english_spanish)
        elif command == "T":
            text_conversion(english_spanish)
        elif command == "Q":
            print("Adios!")
            return
        else:
            print("Unknown command, enter W, A, R, P, T or Q!")
if __name__ == "__main__":
    main()
