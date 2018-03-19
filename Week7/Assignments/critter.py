
__author__ = 'Robert W. Curtiss'
__project__ = 'CS1511'

"""
====================================================
Author: Robert W. Curtiss
Class: CSCI-1511
    Project: CS1511
    File: critter
    Created: Mar, 08, 2018
    
    Description:
    
===================================================
"""
class Critter(object):
    """Virtual pet"""
    total = 0  # class attribute

    def __init__(self, name, hunger=0, boredom=0):
        self.name = name  # public
        self.hunger = hunger  # public
        self.boredom = boredom

    def __pass_time(self):
        self.boredom += 1
        self.hunger += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "happy"
        elif 5 <= unhappiness <= 10:
            m = 'okay'
        elif 11 <= unhappiness <= 15:
            m = "frustrated"
        else:
            m = "mad"
        return m

    def talk(self):
        print("I'm {} and I feel {} now.\n".format(self.name, self.mood))
        self.__pass_time()

    def eat(self, food=4):
        print("Brrupp. Thank you.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 4):
        print(*"Wheee!\n")
        self.boredom -= fun
        if self.boredom <= 0:
            self.boredom = 0
        self.__pass_time()