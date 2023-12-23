"""
Here I am implementing a program of a game where players aim to score exactly 50 points. If a player ends up having more than 50 points, his/her score will be decreased
to 25 points. Here I am also assuming that two players are playing scoring. in main program, two Player type objects are defined and calls the methods get_name,
get_points, has_won, and add_points. In the main function the variables player1 ja player2 are the names given to these two objects. Those names persistently refer to
the same objects. Variable in_turn, on the other hand, switches referring between these two objects depending on whose turn it is (i.e. whether the value of the variable
throw is even or odd).
"""
class Player:
    """ Class Player: Implements a game that where players aim to score exactly 50 points. If a player ends up having more than 50 points, his/her score will be decreased to
    25 points. Here two players are playing."""
    def __init__(self, name, points, number_of_rounds, hit_percentage):
        """ Constructor, initializes the newly created object.
        :param name: string, name of the player
        :param points: int, points entered by the player
        :param number_of_rounds: int, number of throws by the players
        :param hit_percentage: int, validate the input of player to find the successful hit. """
        self.set_name(name)
        self.set_points(points)
        self.set_rounds(number_of_rounds)
        self.set_hit_percentage(hit_percentage)
        self.__total_points = 0
    def get_name(self):
        """Return player's name. """
        return self.__name
    def set_name(self, name):
        """set the name of the player to self.__name. :param name: str, name of the player. """
        self.__name = name
    def get_points(self):
        """Return player's score. :return: float, score of the player."""
        return self.__points
    def set_points(self, points):
        """set the score of the player to self.__score. :param points: int, score of the player. """
        self.__points = points
    def get_rounds(self):
        """Return number of the round. :return: int, number of the round. """
        return self.__rounds
    def set_rounds(self, number_of_rounds):
        """set the round variable to self.__round. :param round: int, round number of the player. """
        self.__rounds = number_of_rounds
    def get_hit_percentage(self):
        """Return hit_percentage. :return: int, hit_percentage of the score. """
        return self.__hit_percentage
    def set_hit_percentage(self, hit_percentage):
        """set the hit_percentage of the player to self.__hit_percentage. :param hit_percentage: int, hit_percentage of the score. """
        self.__hit_percentage = hit_percentage
    def hit_percentage(self):
        """If round is more then one then calculate the hit_percentage"""
        if self.__rounds > 0:
            hit_percentage  = (100 * float(self.__hit_percentage / self.__rounds))
            return hit_percentage
        else:
            return 0.0
    def has_won(self):
        """return True if the player has won the game"""
        if self.__points == 50:
            return True
    # Should return True of False
    def add_points(self, pts):
        """Add points of the player according to the game rules"""
        if pts > 0:
            self.__hit_percentage += 1
        self.__points += pts
        # here accumulating the total points without deducting any scores
        self.__total_points += pts
        # increment the round number
        self.__rounds += 1
        if self.__points > 50:
            print(f"{self.__name} gets penalty points!")
            # set the score to 50 in case total score is above 50.
            self.__points = 25
            return self.__points
        elif self.__points == 50:
            # Player has won the game
            self.has_won()
        elif (self.__points >= 40 and self.__points <= 49):
            print(f"{self.__name} needs only {50 - self.__points} points. "
                  f"It's better to avoid knocking down the pins with higher points.")
    def calculate_avg(self):
        # Trying to take avarage
        if self.__rounds > 1:
            average_of_points = float(self.__total_points/self.__rounds)
            return average_of_points

def main():
    # Here we define two variables which are the objects initiated from the
    # class Player. This is how the constructor of the class Player
    # (the method that is named __init__) is called!
    player1 = Player("Matti", points = 0, number_of_rounds=0, hit_percentage=0)
    player2 = Player("Teppo", points = 0, number_of_rounds=0, hit_percentage=0 )
    throw = 1
    avg_score = 0
    while True:
        # if throw is an even number
        if throw % 2 == 0:
            in_turn = player1
        # else throw is an odd number
        else:
            in_turn = player2
        pts = int(input("Enter the score of player " + in_turn.get_name() +
                        " of throw " + str(throw) + ": "))
        in_turn.add_points(pts)
        in_turn.hit_percentage()
        # c) Here adding a supporting feedback printout "Cheers NAME!".
        avg_score = in_turn.calculate_avg()
        if avg_score is not None:
            if (avg_score < pts and throw > 1):
                print(f"Cheers {in_turn.get_name()}!")
        if in_turn.has_won():
            print("Game over! The winner is " + in_turn.get_name() + "!")
            return
        print("")
        print("Scoreboard after throw " + str(throw) + ":")
        print(player1.get_name() + ":", player1.get_points(), f"p, hit percentage {player1.hit_percentage():.1f}")
        print(player2.get_name() + ":", player2.get_points(), f"p, hit percentage {player2.hit_percentage():.1f}")
        print("")
        throw += 1
if __name__ == "__main__":
    main()
