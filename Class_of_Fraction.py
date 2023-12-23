"""
Here I am implementing a Fraction class. Here I have created the methods complement and reciprocal to the Fraction class. These methods form the complement or the reciprocal
and return their result as a Fraction type object.
Then implemented a new method named multiply, which can be used to calculate the product of two fraction objects. After that, created a division method named divide
for the class. This method takes another fraction object as a parameter and returns the result in a new fraction object. Lastly, the methods add to calculate the sum
and deduct to calculate the difference of two fractions is implemented.
"""
class Fraction:
    """ This class represents one single fraction that consists of numerator and denominator."""
    def __init__(self, numerator, denominator):
        """ Constructor. Checks that the numerator and denominator are of correct type and initializes them.
        :param numerator: int, fraction's numerator
        :param denominator: int, fraction's denominator """
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
        """:returns: str, a string-presentation of the fraction in the format numerator/denominator."""
        if self.__numerator * self.__denominator < 0:
            sign = "-"
        else:
            sign = ""
        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"
    def simplify(self):
        gsd = greatest_common_divisor(self.__numerator, self.__denominator)
        self.__numerator = self.__numerator//gsd
        self.__denominator = self.__denominator//gsd
    def complement(self):
        """ This function will take the compliment of the fraction. :return Fraction, int, compliment of the fraction. """
        return Fraction(-1 * self.__numerator, self.__denominator)
    def reciprocal(self):
        """ This function will take the reciprocal of the fraction. :return Fraction, int, reciprocal of the fraction."""
        new_numerator = self.__denominator
        new_denominator = self.__numerator
        return Fraction(new_numerator, new_denominator)
    def multiply(self, target):
        """ This function will multiply the two fraction objects. :param target, int, the target fraction.
        :return Fraction, int, new fraction that is multiple of two fraction objects."""
        new_numerator = self.__numerator * target.__numerator
        new_denominator = self.__denominator * target.__denominator
        return Fraction(new_numerator, new_denominator)
    def divide(self, target):
        """ This function will divide the two fraction objects. :param target, int, the target fraction.
        :return Fraction, int, new fraction that is division of two fraction objects"""
        new_numerator = self.__numerator * target.__denominator
        new_denominator = self.__denominator * target.__numerator
        return Fraction(new_numerator, new_denominator)
    def expand(self, other):
        """ This function will Expand fractions to have the same denominator."""
        common_denominator = self.__denominator * other.__denominator
        return Fraction(self.__numerator * other.__denominator, common_denominator), Fraction(other.__numerator * self.__denominator, common_denominator)
    def add(self, other):
        """ This function will add the two fraction objects. :param other, int, the second fraction.
        :return Fraction, int, new fraction that is sum of two fraction objects"""
        expanded_self, expanded_other = self.expand(other)
        result_numerator = expanded_self.__numerator + expanded_other.__numerator
        return Fraction(result_numerator, expanded_self.__denominator)

    def deduct(self, other):
        """ This function will minus the two fraction objects.:param other, int, the second fraction.
        :return Fraction, int, new fraction, minus of two fraction objects"""
        expanded_self, expanded_other = self.expand(other)
        result_numerator = expanded_self.__numerator - expanded_other.__numerator
        return Fraction(result_numerator, expanded_self.__denominator)
def greatest_common_divisor(a, b):
    """ Returns the greatest common divisor.  When both the numerator and the denominator is divided by their greatest common divisor,
    the result will be the most reduced version of the fraction in question. """
    while b != 0:
        a, b = b, a % b
    return a



