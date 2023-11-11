"""
Here I am writing code of rock-paper-scissors game for two players. In this game, both players use one letter to tell whether they choose rock (R),
paper (P) or scissors (S). After this, the program shows the result. Paper beats rock, rock beats scissors and scissors beat paper.
Step1: Take inputs from two players
Step2: If inputs are correct, compare the values
Step3: write conditions where Paper beats rock, rock beats scissors and scissors beat paper.
Step4: Display the winner player
"""
def main():
    player_1 = input(str("Player 1, enter your choice (R/P/S): "))
    player_2 = input(str("Player 2, enter your choice (R/P/S): "))
    # If input is correctly entered then compare the values
    if player_1 == "R" or player_1 == "P" or player_1 == "S" and player_2 == "R" or player_2 == "P" or player_2 == "S":
        # Checking for tie. if both players have selected same choice
        if (player_1 == "R" and player_2 == "R") or (player_1 == "S" and player_2 == "S") or (player_1 == "P" and player_2 == "P"):
            print("It's a tie!")
        elif (player_1 == "S" and player_2 == "P") or (player_1 == "R" and player_2 == "S") or (player_1 == "P" and player_2 == "R"):
            print("Player 1 won!")
        elif (player_1 == "R" and player_2 == "P") or (player_1 == "P" and player_2 == "S") or (player_1 == "S" and player_2 == "R"):
            print("Player 2 won!")
    else:
        # Print an error message.
        print("Bad input, Enter again!")
        main()
if __name__ == "__main__":
    main()