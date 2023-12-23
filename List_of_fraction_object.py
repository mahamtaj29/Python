"""
Here I'm implementing a program where the user enters a list of fractions, which prints the fractions in the same order, in a simplified manner.
"""
class Fraction:
    """ This class represents one single fraction that consists of numerator and denominator. """
    def __init__(self, numerator, denominator):
        """ Constructor. Checks that the numerator and denominator are of correct type and initializes them.
        :param numerator: int, fraction's numerator
        :param denominator: int, fraction's denominator. """
        # isinstance is a standard function which can be used to check if a value is an object of a certain class.
        # So, the following test checks that both parameters are ints as they should be in a valid fraction.
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError
        # Denominator can't be zero, not in mathematics, and not here either.
        elif denominator == 0:
            raise ValueError
        self.__numerator = numerator
        self.__denominator = denominator
    def return_string(self):
        """ :returns: str, a string-presentation of the fraction in the format numerator/denominator. """
        if self.__numerator * self.__denominator < 0:
            sign = "-"
        else:
            sign = ""
        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"
    def simplify(self):
        gsd = greatest_common_divisor(self.__numerator, self.__denominator)
        self.__numerator = self.__numerator//gsd
        self.__denominator = self.__denominator//gsd
def greatest_common_divisor(a, b):
    """ This method returns the greatest common divisor.  When both the numerator and the denominator is divided by
    their greatest common divisor, the result will be the most reduced version of the fraction in question. """
    while b != 0:
        a, b = b, a % b
    return a
def user_input():
    """ This function will ask user to enter values of seawater levels. User Input will also be validated by checking
    the number of inputs entered by user. Function will give error if the user input is less than two entries.
    :param No paramter in this function
    :return: list_of_seawater_values, this function will return list of user input."""
    print("Enter fractions in the format integer/integer.\n"
          "One fraction per line. Stop by entering an empty line.")
    list_of_fractions = []
    # counter to check the count of user input
    flag = True
    while flag:
        # Take input from user
        fraction = input()
        if (fraction == ""):
            flag = False
        else:
            numerator, denomenator = fraction.split("/")
            frac = Fraction(int(numerator), int(denomenator))
            list_of_fractions.append(frac)
    # return the user input in form of a list
    return list_of_fractions
def show_simplified(list_of_fractions):
    """
    This function will show the list of fraction object in simplified form
    :param list_of_fractions:list, list of fraction object. """
    print("The given fractions in their simplified form:")
    for frac in list_of_fractions:
        input_value = frac.return_string()
        frac.simplify()
        simplified = frac.return_string()
        print(f"{input_value} = {simplified}")

def main():
    #Function 1: To take input from user and validate the input
    list_of_fractions = user_input()
    show_simplified(list_of_fractions)
if __name__ == "__main__":
    main()




