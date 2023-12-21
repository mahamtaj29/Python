"""
Here I am implementing a program using class that shows person name and electronic wallet. The program has been modified in a way, that the person's address will also be saved as an attribute
of the object. Also, implemented the method move which can be used to change the person's address when he moves into a new apartment, house etc.
"""
class Person:
    """
    This class models a person with a simple electronic wallet.
    """
    def __init__(self, name, initial_money, initial_address):
        """
        A person object is initialized with the name and the initial amount of money in the wallet.
        :param name: str, the name of the person whose spending the object is following.
        :param initial_money: float, how much money will there be in the wallet at the point of creation.
        :param initial_address: string, the address of the person.
        """
        self.__name = name
        self.__money = initial_money
        self.__address = initial_address
    def printout(self):
        """
        When a person's data is needed to be printed on screen this method will handle it.  Also good for debugging and testing purposes.
        """
        print("—" * 25)
        print("Name:   ", self.__name)
        print("Wealth: ", self.__money)
        print("Address:", self.__address)
    def add_money(self, amount):
        """
        It is possible to add money in the electronic wallet.
        :param amount: float, the amount of money added.
        :return: True if operation successfull False otherwise.
        """
        if amount < 0.0:
            return False
        else:
            self.__money += amount
            return True
    def make_payment(self, price):
        """
        When making a payment, money needs to be deducted from the person's wallet.
        :param price: float, the price of the purchase
            i.e. how much money to deduct from the wallet.
        """
        if price < 0.0:
            print("The price can't be negative.")
        elif price > self.__money:
            print("You can't afford that.")
        else:
            self.__money -= price
    def move(self, current_address):
        """
        Address will be updated when a person change the location.
        :param current_address: str, the new location of a person
        """
        if current_address != self.__address:
            self.__address = current_address

def main():
    # Let's create an object of type Person, name it Mike, and see the Mike's spending.
    Mike = Person("Mike Daniel", 100.00, "320 Memorial Dr.")
    Mike.printout()
    # Mike moves out of a dormitory to a place of his own.
    Mike.move("20 Chestnut St.")
    # Where's Mike after the move.
    Mike.printout()

if __name__ == "__main__":
    main()
