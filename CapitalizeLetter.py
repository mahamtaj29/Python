"""
Here I am implementing a function that will take input from user & print the text by capitalizing first letter of each word.
"""
def capitalize_initial_letters(user_input):
    """
    This function will take input from user & print the text by capitalizing
    first letter of each word.
    :param user_input: string type. It is the input entered by the user
    :return: capital_initial_letter string, the function will return the string
    with capital letter of each word.
    """
    # Using the str.title() function to capitalize first letter of each word.
    user_input = user_input.title()
    return user_input

def main():
    user_input = input("Enter the word, you want to capitalize first letter: ")
    print(capitalize_initial_letters(user_input))
if __name__ == "__main__":
    main()
