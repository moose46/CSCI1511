"""
====================================================
Author: Robert W. Curtiss
Class: CSCI-1511
    Project: CS1511
    File: Coin
    Created: Mar, 06, 2018
    
    Description:
    Coin Class
===================================================
"""
import random as rnd


class Coin(object):
    __sideup = None
    __amount = 20

    def __str__(self):
        self.toss()

    def toss(self):
        self.__sideup = rnd.choice(['heads', 'tails'])

    def get_amount(self):
        return self.__amount

    def add_one(self):
        self.__amount += 1

    def take_one(self):
        self.__amount -= 1

    def get_side_up(self):
        return self.__sideup
