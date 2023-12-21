"""
Here I am implementing a program that reads the TV series from a file, where the format of every row is name;genres and genres are separated using commas.
Firstly I printed all the genres found from the file in an alphabetic order.  After this, the program waits for the user's input and user enters one of the genres.
The program then prints the user all the series marked to the genre in question.
"""
def read_file(filename):
    """
    :param filname is the parameter for this function. The text file contains the names of the series and their genres.
    :return genre_entire_dict is the return value which contains the dictionary with all the series and their genres.
    """
    # Initializing a new data structure
    genre_entire_dict = {}
    try:
        file = open(filename, mode="r")
        for row in file:
            name, genres = row.rstrip().split(";")
            genres = genres.split(",")
            # adding the name and genres data to the data structure
            for index in range(len(genres)):
                if genres[index] not in genre_entire_dict.keys():
                    genre_entire_dict[genres[index]] = []
            for index in range(len(genres)):
                genre_entire_dict[genres[index]].append(name)
        file.close()
        # returning the data structure
        return genre_entire_dict
    except ValueError:
        print("Error: rows were not in the format name;genres.")
        return None
    except IOError:
        print("Error: the file could not be read.")
        return None

def main():
    filename = input("Enter the name of the file: ")
    genre_data = read_file(filename)
    available_genre = ", ".join(sorted(genre_data.keys()))
    print("Available genres are:", available_genre)
    while True:
        genre = input("> ")
        if genre == "exit":
            return
        else:
            # Printing genres in Alphabetical order
            if genre in genre_data.keys():
                series = sorted(genre_data.get(genre))
                for index in range(len(series)):
                    print(series[index])
if __name__ == "__main__":
    main()
