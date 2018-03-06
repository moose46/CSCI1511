"""
====================================================
Author: Robert W. Curtiss
Class: CSCI-1511
    Project: CS1511
    File: critters-robertcurtiss
    Created: Mar, 06, 2018
    
    Description:
    Critters, using OOP
===================================================
"""


class Critter(object):
    """Virtual pet"""
    total = 0  # class attribute

    def __init__(self, name='Bob', mood="Happy as a clam"):
        self.__name = name  # private
        self.__mood = mood  # private
        print("A {} critter has been born!\n".format(self.__mood))
        Critter.total += 1

    def talk(self):
        print("Hello, I'm {}!\n".format(self.name))

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("Name can not be empty!")
        else:
            self.__name = new_name
            print("Name change successful!")

    def __str__(self):
        return "Critter Object:\n" + "Name: " + self.name + "\n"

    @staticmethod
    def status():
        print("\nThe total number of critters is: {}".format(Critter.total))


crit1 = Critter('Bob')
crit1.talk()
crit2 = Critter('Dave', "Ugly")
crit2.talk()
crit2.name = "Bozo"
print(crit1)
print(crit2)

crit2.status()
