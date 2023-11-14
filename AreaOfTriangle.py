"""
Here I am writing a program to calculate the area of the triangle.
"""
import math
from math import sqrt
def area (a, b, c):
    """this function will calculate the area of the triangle"""
    add_value = (a + b + c)
    value_of_s = float(add_value) / 2
    area = value_of_s * ((value_of_s - a) * (value_of_s - b) * (value_of_s - c))
    calculated_area = float(math.sqrt(area))
    return calculated_area
def main():
    line_one = input("Enter the length of the first side: ")
    line_two = input("Enter the length of the second side: ")
    line_three = input("Enter the length of the third side: ")
    a = (float(line_one))
    b = (float(line_two))
    c = (float(line_three))
    calculated_area = area(a, b, c)
    print(f"The triangle's area is {calculated_area:1.1f}")


if __name__ == "__main__":
    main()
