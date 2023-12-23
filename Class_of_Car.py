"""
Here I am implementing a class Car. The main function also includes an object of the Car class and a call of the method print_information.  I have added attributes called __gas
and __odometer in the class. These attributes are used for saving the internal state of the car object, i.e. the amount of gas in the car's tank and the number of kilometers
in the car's odometer. The constructor initiates values that ensure that the tank is empty and the odometer shows a zero.
The method print_information prints how much gas the car's tank contains and what does the car's odometer show.The information is printed to the specificity of one decimal.
The car refuelling/fill method uses the amount of refuelled gas as a parameter. The Car class ensures that fuel can't surpass the size of the tank.
The drive method uses information on how many kilometers to drive as a parameter.
"""
class Car:
    """ Class Car: Implements a car that moves a certain distance and whose gas tank can be filled. The class defines what a car is: what information it contains and
    what operations can be carried out for it."""
    def __init__(self, tank_size, gas_consumption, amount_of_gas, odometer, kilometers_to_drive):
        """ Constructor, initializes the newly created object.
        :param tank_size: float, the size of this car's tank.
        :param gas_consumption: float, how much gas this car consumes when it drives a 100 kilometers.
        :param amount_of_gas: float, how much gas the user wants to fill
        :param odometer: float, odometer is the distance covered by car
        :param kilometers_to_drive: int , the distance that user wants to travel """
        self.__tank_volume = tank_size
        self.__consumption = gas_consumption
        self.__amount_of_gas = amount_of_gas
        self.__odometer = odometer
        self.__to_drive = kilometers_to_drive
    def print_information(self):
        """ This function will print the distance and amount of gas used by car. """
        print(f"The tank contains {self.__amount_of_gas:.1f} liters of gas and the odometer shows {self.__odometer:.1f} kilometers.")
    def fill(self, amount_of_gas):
        """ This function will ask user to enter the amount of gas to be filled
        :param amount_of_gas: float, the amount of gas to be filled.
        :return amount_of_gas: float, updated value of gas in the tank. """
        if amount_of_gas > 0:
            self.__amount_of_gas += amount_of_gas
            if self.__amount_of_gas > self.__tank_volume:
                self.__amount_of_gas = self.__tank_volume
                return self.__amount_of_gas
        else:
            print("You cannot remove gas from the tank")
            return self.__amount_of_gas
    def drive(self, distance):
        """ This function will ask the user to enter the distance that user wants to cover by car.
        :param distance: int, the distance to cover by car
        :param odometer: float, updated value in odometer showing the distance covered by car. """
        self.__amount_of_gas -= int(distance/10)
        if self.__amount_of_gas < 0:
            self.__amount_of_gas = 0.0
        if distance > 0:
            self.__odometer += distance
            if (self.__amount_of_gas == 0 and self.__odometer > 100):
                self.__odometer = 100
                return self.__odometer
        else:
            print("You cannot travel a negative distance")
def main():
    tank_size = read_number("How much does the vehicle's gas tank hold?")
    gas_consumption = read_number("How many liters of gas does the car "
                                  "consume per hundred kilometers?")
    amount_of_gas = 0.0
    odometer = 0.0
    kilometers_to_drive = 0
    car = Car(tank_size, gas_consumption, amount_of_gas, odometer, kilometers_to_drive)
    while True:
        car.print_information()
        choice = input("1) Fill 2) Drive 3) Quit\n-> ")
        if choice == "1":
            to_fill = read_number("How many liters of gas to fill up?")
            car.fill(to_fill)
        elif choice == "2":
            distance = read_number("How many kilometers to drive?")
            car.drive(distance)
        elif choice == "3":
            print("Thank you and bye!")
            break
def read_number(prompt, error_message="Incorrect input!"):
    """ This function is used to read input (float) from the user.
    :param prompt: str, prompt to be used when asking user input.
    :param error_message: str, what error message to print, if the entered value is not a float.
    """
    while True:
        try:
            return float(input(prompt + " "))
        except ValueError:
            print(error_message)
if __name__ == "__main__":
    main()
