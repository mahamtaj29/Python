"""
Here I am implementing the function longest_substring_in_order, which takes a string as its parameter and searches for the
longest substring with its characters in alphabetic order and then returns it. Assuming that string contains only lower-case letters,
so comparison can be taken of the alphabetical order of the strings by using the comparison operator <.
"""
def longest_substring_in_order(user_input):
    """
    This function takes a string as its parameter and searches for the longest substring with its characters in alphabetic order and then returns it.
    :param user_input: str which is a user input
    :return: max_substring, str, which is the maximum substring
    """
    if len(user_input) <= 1:
        return user_input
    # here The function returns its parameter value when it is an empty string or a string made of a single character.
    max_substring = user_input[0]
    # assign first value to max_substring and current_substring
    current_substring = user_input[0]
    for index in range(1, len(user_input)):
        # comparison of two values
        if user_input[index] >= user_input[index-1]:
            current_substring += user_input[index]
        else:
            # if current_substring is greater than equal it to max_substring
            if len(current_substring) > len(max_substring):
                max_substring = current_substring
            # replace current_substring to next index
            current_substring = user_input[index]
    # here final check to find the max_string
    if len(current_substring) > len(max_substring):
        max_substring = current_substring
    return max_substring
def main():
    user_input = "xyzstuopqklmefgabc"
    print(longest_substring_in_order(user_input))
if __name__ == "__main__":
    main()