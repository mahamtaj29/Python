"""
Here I am implementing a program that reads 5 numbers a user enters and then prints the numbers that are greater than
zero.
"""
def main():
    """ This function will first read 5 numbers a user enters and then prints,
     all the numbers that are greater than zero.
     :param numbers_list is an empty list
     :param next_numbers has the new entered inputs
     append has been used to add the numbers into the list in order"""
    numbers_list = []
    print("Enter 5 numbers that you want to print:")
    for numbers in range(0, 5, 1):
        next_numbers = int(input("Enter here: "))
        numbers_list.append(next_numbers)
    print("The numbers that are greater than zero are:")
    for each_index in numbers_list:
        if each_index > 0:
            print(each_index)

if __name__ == "__main__":
    main()
