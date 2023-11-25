"""
This program asks user to enter a file name and then prints the contents of that file on the screen with line number.
Error message is printed if there are any problems opening the file.
"""
def main():
    filename = input("Enter the name (text.txt) of the file: ")
    # The code lines which might cause an error are placed inside try.
    try:
        file = open(filename, mode="r")
        counter = 0
    except OSError:
        print(f"There was an error in reading the file.")
        return
    for file_line in file:
        file_line = file_line.rstrip()
        counter += 1
        print(f"{counter} {file_line}")
    # When the file has been processed, we should close it.
    file.close()

if __name__ == "__main__":
    main()
