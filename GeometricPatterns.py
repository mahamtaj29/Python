"""
In this code, I am implementing a program that prompts the user to select a geometric pattern (a square or a rectangle)
and enter the required dimensions. The program prints the circumference and area of the pattern to two decimal places.
The program first prints a menu where the user can select their desired pattern or stop the program
(s = square, r = rectangle and q = quit). If something other than n, s or q is entered, the program prints error message
"Incorrect entry, try again!" and returns to the pattern selection. If a negative number or a zero is entered as a dimension,
the user is asked to re-enter the value, using the same prompt as originally.
"""
from math import pi
def check_input(input_value,message):
    """This function is created to check the input if it is greater than zero. Otherwise
    this function will ask the user to enter the value again"""
    flag = True
    while flag:
        input_value = float(input(message))
        if input_value > 0:
            flag = False
            break
        else:
            flag = True
    return input_value

def square_calculation(s_length):
    """This function will calculate the surface area and circumference of the square.
    The function will take one parameter (length) to calculate the area and circumference.
    This function also returns the area and circumference values. The parameters can be integer or float values """
    square_area = s_length * s_length
    square_circum = 4 * s_length
    display_message(square_area, square_circum)
    return square_area, square_circum

def rectangle_calculation(width, height):
    """This function will calculate the surface area and circumference of the rectangle.
    The function will take two parameters (height & width) of the rectangle to calculate the area
    and circumference. This function also returns the area and circumference of the rectangle. The
    parameters can be integer or float values """
    rectangle_area = width * height
    rectangle_circum = 2 * (width + height)
    display_message(rectangle_area, rectangle_circum)
    return rectangle_circum, rectangle_area

def circle_calculation(radius):
    """This function will calculate the surface area and circumference of the circle.
        The function will take one parameter (radius) to calculate the area and circumference.
        This function also returns the area and circumference. The parameter can be integer or float value """
    circle_area = pi * (radius * radius)
    circle_circum = 2 * pi * radius
    display_message(circle_area, circle_circum)
    return circle_circum, circle_area

def display_message(area, circumference):
    """This function will display the area and circumference calculated in other functions"""
    print(f"The circumference is {circumference:.02f}")
    print(f"The surface area is {area:.02f}")
def select_pattern():
    """This function will ask the user to select the pattern"""
    flag = True
    while True:
        answer = input("Enter the pattern's first letter (r or s) or (q)uit: ")
        if answer == "s":
            value = 0.0
            result = check_input(value, "Enter the length of the square's side: ")
            square_calculation(result)
        elif answer == "r":
            value = 0.0
            first_value = check_input(value, "Enter the length of the rectangle's side 1: ")
            second_value = check_input(value, "Enter the length of the rectangle's side 2: ")
            rectangle = rectangle_calculation(first_value, second_value)
        elif answer == "c":
            value = 0.0
            result = check_input(value, "Enter the circle's radius: ")
            circle_calculation(result)
        elif answer == "q":
            return

        else:
            print("Incorrect entry, try again!")
        print()
def menu():
    """This function will call another function to take input from user. This function has
    no parameters and it will not return any parameter as well."""
    select_pattern()

def main():
    menu()
    print("Goodbye!")

if __name__ == "__main__":
    main()
