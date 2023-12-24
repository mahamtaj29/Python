"""
Here I am developing the class Character of a game that have some items in the backpack. Often in video games, when there are multiple
characters, they also have some kind of interaction with each other. Sometimes characters have a fight. If there is no fight between characters then
the characters in a game can pass items between each other. Let's see how these kind of interactions could be implemented in our Character class.
"""
class Character:
    """ This class defines the available weapons for two characters of the game. """
    def __init__(self, name, hit_points):
        """ :param name: str, the name of the character.
        :param hit_points: int, points of the character. """
        self.__name = name
        self.__hit_point = hit_points
        self.__skills = {}
    def printout(self):
        """This function will print the name and hitpoints of the character and the skills of the character."""
        print("Name:", self.__name)
        print("Hitpoints:", self.__hit_point)
        if self.__skills:
            for skill in sorted(self.__skills):
                print(f"  {self.__skills[skill]} {skill}")
        else:
            print(f"  --nothing--")
    def give_item(self, item):
        """This function will check the count of the items in the dictionary of weapons and calculate the total items.
        :param item, string, name of weapon. """
        counter = 1
        if item not in self.__skills.keys():
            # create empty space against the key
            self.__skills[item] = counter
        else:
            counter = self.__skills[item]
            # increment the count of the weapon
            counter += 1
            updated = {item: counter}
            self.__skills.update(updated)
    def remove_item(self, item):
        """This function will remove the item from the dictionary of weapons.:param item, string, name of weapon.
        :return True or False"""
        value = 0
        if item not in self.__skills.keys():
            return
        else:
            value = self.__skills[item]
            if value > 1:
                value -= 1
                updated = {item: value}
                self.__skills.update(updated)
            else:
                del self.__skills[item]
    def get_name(self):
        """This function will return the name of the character.:return self.__name str, name of the character"""
        return self.__name
    def has_item(self, item):
        """This function will check if the item is present in the dictionary of weapons and return True or False.
        :param item, string, name of weapon.
        :return True or False"""
        if item in self.__skills.keys():
            return True
        else:
            return False
    def how_many(self, item):
        """This function will check if the item is present in the dictionary and return the count of items.
        :param item, string, name of weapon.
        :return int , count of items """
        if item in self.__skills.keys():
            return self.__skills[item]
        else:
            return 0
    def pass_item(self, item, target):
        """ This function will check if the item is present in the dictionary of weapons and return True or False.
        :param item, string, name of weapon.
        :param target, str name of the weapon to be used for attack
        :return int , count of items"""
        if item not in self.__skills.keys():
            return False
        else:
            # calling the remove function to remove the weapon from attacker
            self.remove_item(item)
            # calling the give function to give the weapon to other character
            target.give_item(item)
            return True
    def attack(self, target, weapon):
        """This function will check the attack by the chararcters and print the message accordingly.
        :param weapon, string, name of weapon.
        :param target, str name of the weapon to be used for attack
        :return int , count of items
        """
        if (weapon not in self.__skills.keys() and weapon in WEAPONS.keys()):
            print(f"Attack fails: {self.__name} doesn't have \"{weapon}\".")
            return False
        if (weapon not in self.__skills.keys() and weapon not in WEAPONS.keys()):
            print(f"Attack fails: unknown weapon \"{weapon}\".")
            return False
        if (self == target):
            print(f"Attack fails: {self.__name} can't attack him/herself.")
            return False
        # Take out points against the weapons
        points_to_remove = WEAPONS[weapon]
        # Remove the points from the score
        target.__hit_point = target.__hit_point - points_to_remove
        print(f"{self.__name} attacks {target.__name} delivering {points_to_remove} damage.")
        if (target.__hit_point <=0):
            print(f"{self.__name} successfully defeats {target.__name}.")
WEAPONS = {
    # Weapon          Damage
    #--------------   ------
    "elephant gun":     15,
    "Simple basic gun":               5,
    "light saber":      50,
    "sword":             7,
}
def main():
    conan = Character("Conan the Barbarian", 10)
    deadpool = Character("Deadpool", 45)
    # Testing the pass_item method
    for test_item in ["sword", "sausage", "plate armor", "sausage", "sausage"]:
        conan.give_item(test_item)
    for test_item in ["gun", "sword", "gun", "sword", "hero outfit"]:
        deadpool.give_item(test_item)
    conan.pass_item("sword", deadpool)
    deadpool.pass_item("hero outfit", conan)
    conan.pass_item("sausage", deadpool)
    deadpool.pass_item("gun", conan)
    conan.pass_item("sausage", deadpool)
    deadpool.pass_item("gun", conan)
    print("-" * 5, "How are things after passing items around", "-" * 20)
    conan.printout()
    deadpool.printout()
    # Testing a fight i.e. the attack method
    print("-" * 5, "Let's see how a fight proceeds", "-" * 32)
    # Conan's turn
    conan.attack(deadpool, "sword") # Conan doesn't have a sword.
    conan.attack(conan, "gun")      # A character is not allowed to attack himself.
    conan.attack(conan, "pen")      # Pen is not a known weapon in WEAPONS dict.
    conan.attack(deadpool, "gun")   # Attack with a gun.
    # Deadpool retaliates
    deadpool.attack(conan, "sword") # Deadpool has a sword.
    # Conan's 2nd turn
    conan.attack(deadpool, "gun")   # Attack with a gun again.
    # Deadpool strikes back again and Conan drops "dead".
    deadpool.attack(conan, "sword")
    print("Are You Not Entertained?!")
    print("-" * 5, "How are things after beating each other up", "-" * 20)
    conan.printout()
    deadpool.printout()
if __name__ == "__main__":
    main()
