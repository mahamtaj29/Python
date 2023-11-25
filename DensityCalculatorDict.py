"""
Here I am implement a word density calculator that reads a piece of text from the user and then prints how many times each of the words appears in the text.
The words in the list are printed in alphabetic order and all the letters are in lower-case. A string separated from other strings with empty characters is considered a word.
"""
def read_message():
    """
    This function will ask user to enter a message.Function will terminate if empty space is entered.
    :param No paramter in this function
    :return: list_of_user_input, string this function will return list of user input.
    """
    # Here creating an empty list
    list_of_user_input = []
    print("Enter rows of text for word counting. Empty row to quit. ")
    flag = True
    while flag:
        # Taking input from user
        user_input = input().lower()
        # Terminating the code, in case of empty input
        if user_input == "":
            flag = False
        else:
            list_of_user_input.append(user_input)
            sorted(list_of_user_input)
    # Returning the user input in form of a list
    return " ".join(list_of_user_input)
def check_word_density(user_list):
    """
    This function will count the occurrence of a word in the text.
    :param my_list: str list.
    :return: dictionary named Ferq
    """
    # Creating an empty dictionary named Frequency
    freq = {}
    for items in user_list:
        freq[items] = user_list.count(items)
    sorted(freq)
    for key in sorted(freq):
        print(f"{key} : {freq[key]} times")
    return freq
def main():
    user_list = read_message()
    word_count = check_word_density(user_list.split())
if __name__ == "__main__":
    main()
