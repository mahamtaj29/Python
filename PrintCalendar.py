"""
Here I am writing a program that asks user to enter month, year and the weekday of the first day of the month
and then prints a calendar which looks like this:
  2020-09
  Mo Tu We Th Fr Sa Su
      1  2  3  4  5  6
   7  8  9 10 11 12 13
  14 15 16 17 18 19 20
  21 22 23 24 25 26 27
  28 29 30
"""
def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
def calculate_month_length(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif is_leap_year(year):
        return 29
    else:
        return 28
def print_calendar(mm, yyyy, start_wday):
    # here variables are initialized to take care of new lines
    MON, SUN = 0, 6
    print(f"{yyyy}-{mm:02d}")
    print("Mo Tu We Th Fr Sa Su")
    # this step is ensuring the spaces before each row.
    print(" " * 3 * start_wday, end="")
    # this function will count the days of each month
    number_of_days = calculate_month_length(mm, yyyy)
    #this function will return the days
    current_wday = start_wday
    # this loop will print all days in a month
    for day in range(1, number_of_days + 1):
        print(f"{day:2} ", end="")
        if current_wday == SUN:
            print()
            current_wday = MON
        else:
            current_wday += 1
def read_integer(message, min_value, max_value):
    """This function will take input till it gets the required input"""
    while True:
        result = int(input(f"{message} [{min_value}-{max_value}] "))
        if min_value <= result <= max_value:
            return result
        else:
            print(f"You entered a bad value (must be between {min_value}-{max_value})")
def read_inputs():
    """This function will take call read_integer function and assign the value to a
    particular variable in order to send it back to the main function"""
    yyyy = read_integer("Select any year between", 1900, 2500)
    mm = read_integer("Select the month", 1, 12)
    weekday = read_integer("Enter the 1st weekday (0 = Mon, 1 = Tue, etc.)", 0, 6)
    return mm, yyyy, weekday

def main():
    month, year, starting_weekday = read_inputs()
    print_calendar(month, year, starting_weekday)
if __name__ == "__main__":
    main()
