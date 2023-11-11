"""
Here I am practicing my first python examples
First example: Printing string
Second example: Taking input from user, perform arthmetic operation and printing
Third example: Converting Fahrenheit to Celsius
"""

# First example
print("Hello World! My name is Maham Taj")

# Second example
age_string = input("Enter age: ")
age = int(age_string)
# add 2 in the age
age += 2
print("The age is", age, "years.")

# Third example
input_line = input("Enter Fahrenheit temp: ")
fahrenheit = float(input_line)
celsius = (fahrenheit - 32) * 5 / 9
print("Temperature in celsius is: ", celsius, "degree")