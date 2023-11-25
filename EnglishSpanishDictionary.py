"""
Here I am implementing a simple dictionary to help a tourist while abroad.  The dictionary contains three useful words,
which are spanish translation of english words "hey, thanks, home". In addition I'll also implement the functions search word,
add word, remove word, print word and translate word using the dictionary.
"""
def main():
    english_spanish = {
        "hey": "hola",
        "thanks": "gracias",
        "home": "casa"
    }
    while True:
        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")
        if command == "W":
            display_word = input("Enter the word to be translated: ")
            # Searching the word from dictionary using get operator
            word = english_spanish.get(display_word)
            if word not in english_spanish.values():
                print("The word", display_word, "could not be found from the dictionary.")
            else:
                print(f"{display_word} in Spanish is {english_spanish[display_word]}")
        elif command == "A":
            english_word = input("Give the word to be added in English: ")
            spanish_word = input("Give the word to be added in Spanish: ")
            # here new entity has been created to update in the dictionary
            new_entry = {english_word: spanish_word}
            english_spanish.update(new_entry)
        elif command == "R":
            remove_word = input("Give the word to be removed: ")
            if remove_word in english_spanish.keys():
                del english_spanish[remove_word]
            else:
                print("The word", remove_word, "could not be found from the dictionary.")
        elif command == "P":
            # Command P prints all the words contained by the dictionary in an alphabetical order according to the English word
            for word in sorted(english_spanish):
                print(word, english_spanish[word])
        elif command == "T":
            # The command T translates an entire sentence instead of one word.
            enter_text = input("Enter the text to be translated into Spanish (use lower case letters): ")
            # creating an empty list and split the user text
            empty_list = []
            empty_list = enter_text.split()
            print("The text, translated by the dictionary: ")
            for index in range(len(empty_list)):
                list_entity = empty_list[index]
                # here take the values from Dict using get
                result = english_spanish.get(list_entity)
                # if word is not in Dict then print it as it is
                if result is None:
                    result = list_entity
                print(result, end=" ")
            print()
            # if quit option has been selected
        elif command == "Q":
            print("Adios!")
            return
        else:
            print("Unknown command, enter W, A, R, P, T or Q!")
if __name__ == "__main__":
    main()
