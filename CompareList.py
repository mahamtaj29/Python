"""
Here I am writing a function that compares the members of the list and return true if the list has same members.
"""

def are_all_members_same(check_list):
    """Read the list and confirm if all members of the list are same or not
    :param same_entry will remain True if all numbers are same.
    :param index is initialized to see the value on each index
    :return: bool value, bool will be true if all numbers are same.
    """
    same_entry = True
    index = 0
    while index < len(check_list):
        if check_list[0] == check_list[index]:
            index += 1
            same_entry = True
        else:
            index += 1
            same_entry = False
            break
    return same_entry

def main():

    sample_list_two = [5, 5, 5, 5, 4, 6, 5, 5, 5]
    print(f"Original list is: {sample_list_two}")
    print("After comparing the members of a list, the result is: ")
    list = are_all_members_same(sample_list_two)
    print(list)
if __name__ == "__main__":
    main()
