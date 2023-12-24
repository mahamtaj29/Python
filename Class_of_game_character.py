"""
In many videogames the player is controlling a character who has many kinds of skills and who often carries all sorts of items with him. Here I will implement a program showing
the characters in the game and available items in their backpacks.
"""
class Character:
    """ This class defines the available weapons for two characters of the game"""
    def __init__(self, name):
        """ :param name: str, the name of the character."""
        self.__name = name
        self.__skills = {}
    def printout(self):
        """ This function will print the name of the character and the skills of the character."""
        print("Name:", self.__name)
        if self.__skills:
            # if skill is present then print the skills
            for skill in sorted(self.__skills):
                print(f"  {self.__skills[skill]} {skill}")
        else:
            print(f"  --nothing--")
    def give_item(self, item):
        """ This function will check the count of the items in the dictionary of weapons and calculate the total items. :param item, string, name of weapon."""
        counter = 1
        if item not in self.__skills.keys():
            # create empty space against the key
            self.__skills[item] = counter
        else:
            counter = self.__skills[item]
            # increment the count of weapon
            counter += 1
            # update the count of weapon in dictionary
            updated = {item: counter}
            self.__skills.update(updated)
    def remove_item(self, item):
        """ This function will remove the item from the dictionary of weapons. :param item, string, name of weapon. :return True or False. """
        value = 0
        if item not in self.__skills.keys():
            return
        else:
            value = self.__skills[item]
            # checking the count of weapons, if weapon is more than one then minus 1 items
            if value > 1:
                value -= 1
                # update the count of weapon
                updated = {item: value}
                self.__skills.update(updated)
            else:
                # if weapon equals zero then delete the item
                del self.__skills[item]
    def get_name(self):
        """ This function will return the name of the character. :return self.__name str, name of the character"""
        return self.__name
    def has_item(self, item):
        """ This function will check if the item is present in the dictionary of weapons and return True or False. :param item, string, name of weapon.
        :return True or False. """
        if item in self.__skills.keys():
            return True
        else:
            return False
    def how_many(self, item):
        """ This function will check if the item is present in the dictionary and return the count of items. :param item, string, name of weapon.
        :return int , count of items"""
        if item in self.__skills.keys():
            return self.__skills[item]
        else:
            return 0
def main():
    character1 = Character("Conan the Barbarian")
    character2 = Character("Deadpool")
    for test_item in ["sword", "sausage", "plate armor", "sausage", "sausage"]:
        character1.give_item(test_item)
    for test_item in ["gun", "sword", "gun", "sword", "Hero outfit"]:
        character2.give_item(test_item)
    character1.remove_item("sausage")
    character2.remove_item("hero outfit")
    character1.printout()
    character2.printout()
    for hero in [character1, character2]:
        print(f"{hero.get_name()}:")
        for test_item in ["sausage", "sword", "plate armor", "gun", "hero outfit"]:
            if hero.has_item(test_item):
                print(f"  {test_item}: {hero.how_many(test_item)} found.")
            else:
                print(f"  {test_item}: none found.")
if __name__ == "__main__":
    main()
