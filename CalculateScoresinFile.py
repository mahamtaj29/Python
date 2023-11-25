"""
Here I am creating a program that helps add up the scores that various contestants have obtained in a game. The scores are stored in a text file that the program uses as input.
The scores can be entered to the file in practically any order, and the program does not even take a stand on how many scores each contestant gets.
The only operations the program performs are the calculation of the sum of scores of the contestants with the same name and printing the scores of all the contestants
in alphabetical order, according to the player's name. The project folder contains the file game.txt with the following content:
essi 5
pietari 9
essi 2
pietari 10
pietari 7
aps 25
essi 1
"""
def calculate_score():
    """
    This function will count the score of the participants.
    """
    filename = input("Enter the name (game.txt) of the score file: ")
    try:
        file = open(filename, mode="r")
    except OSError:
        print("There was an error in reading the file.")
        return
        # Initialize the dictionary and a list for the entries.
    players_score = {}
    # Populate the dictionary, until the file has been processed.
    for file_line in file:
        # Remove the character(s) that end the line.
        file_line = file_line.rstrip()
        # Split the line in two values.
        try:
            name, score = file_line.split(" ")
        except ValueError:
            print("There was an erroneous line in the file:")
            print(file_line)
            return
        # Add a new entry to the players_score.
        try:
            if name in players_score:
                players_score[name] = int(players_score[name]) + int(score)
            else:
                players_score[name] = int(score)
        except ValueError:
            print("There was an erroneous score in the file:")
            print(score)
            return
    file.close()
    return players_score

def main():
    finding_score = calculate_score()
    if finding_score != True:
        print("Contestant score:")
        for item in sorted(finding_score):
            print(f"{item} {finding_score[item]}")
    else:
        return
if __name__ == "__main__":
    main()

