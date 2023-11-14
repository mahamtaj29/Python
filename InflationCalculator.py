"""
Here I am writing a program which can be used to figure out the maximum inflation increase from the values entered by the user.
In other words: the largest difference between the consecutive entered values.
"""
def main():
    flag = True
    user_input = 0.0
    first_entered_value = 0.0
    second_entered_value = 0.0
    largest_gap = 0.0
    inflation_gap = 0.0
    number = 1
    #This loop will take the input from user till enter is pressed
    while flag:
        user_input = input(f"Enter inflation rate for month {number}: ")
        if number <= 2 and user_input == "":
            print("Error: at least 2 monthly inflation rates must be entered.")
            break
        elif number ==1 and user_input != "":
            first_entered_value = abs(float(user_input))
            number = number + 1
        elif (number >= 2):
            if (user_input == ""):
                print(f"Maximum inflation rate change was {largest_gap:0.1f} points.")
                break
            else:
                second_entered_value = abs(float(user_input))
                inflation_gap = second_entered_value - first_entered_value
            if (largest_gap == 0 or largest_gap < inflation_gap):
                largest_gap = inflation_gap
            number = number + 1
            first_entered_value = second_entered_value
        else:
            flag = False
if __name__ == "__main__":
    main()
