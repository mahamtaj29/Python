"""
Here I am writing a program that will print the even numbers between 0 to 100 first in ascending order & then in descending order.
"""
def even_numbers(starting_number, ending_number, increment):
    """ This function will print the even numbers between 0 to 100
    first in ascending order & then in descending order.
    :param starting_number is int variable
    :param ending_number is int variable
    :param increment is also int variable
    """
    for counter in range(starting_number, ending_number, increment):
        if counter % 2 == 0:
            print(f"{counter}", end=" ")
def main():
    starting_number, ending_number, increment = 0, 101, 1
    even_numbers(starting_number, ending_number, increment)
    starting_number, ending_number, increment = 101, -1, -1
    even_numbers(starting_number, ending_number, increment)

if __name__ == "__main__":
    main()
