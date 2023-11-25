"""
Here I am implementing a program that reads an user message, ending with an empty line, and then saves it to a file so that the file also contains line numbers.
Finally, the program should print an announcement of the file being written or, alternatively, an announcement that writing to the file did not succeed.
"""
def read_message():
    """
    This program asks user to enter a file name and then writes the contents in that file.
    Error message is printed if there are any problems occurs in opening the file.
    """
    string_list = []
    counter = 0
    try:
        # To be able to write into file the value of the mode parameter for open must be "w" (write).
        filename = input("Enter the name of new file: ")
        save_file = open(filename, mode="w")
    except OSError:
        print(f"Writing the file {filename} was not successful.")
        return
    print("Enter rows of text. Quit by entering an empty row.")
    while True:
        text_line = input()
        if text_line == "":
            break
        else:
            string_list.append(text_line)
    for index in range(len(string_list)):
        counter += 1
        print(counter, string_list[index], file=save_file)
    save_file.close()
    print(f"File {filename} has been written.")
    return string_list

def main():
    read_message()
if __name__ == "__main__":
    main()

