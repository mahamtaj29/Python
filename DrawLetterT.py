"""
Here I am writing a program that takes height as input from user and draws a letter T.
"""
def main():
    print("Hello! I draw letter t.")
    # Read the drawing character.
    char = input("Please, enter the drawing character: ")
    # Read the height of the letter and convert the input to an integer.
    height_as_string = input("Please, enter the height of the drawing: ")
    height = int(height_as_string)
    # Validating if the height is odd and greater than two in order to draw T.
    if height % 2 == 1 and height > 2:
        # Print the horizontal line.
        print(height * char)
        # Determine the number of spaces preceding the character of the vertical line.
        nspaces = height // 2
        # Print the vertical line.
        for ind in range(0, height - 1):
            print(nspaces * " " + char)
    # If height is an even number or less than 2 then print the error message.
    else:
        print("Invalid height!")
if __name__ == "__main__":
    main()