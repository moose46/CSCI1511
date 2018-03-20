__author__ = 'Robert W. Curtiss'
__project__ = 'CS1511'

"""
====================================================
Author: Robert W. Curtiss
Class: CSCI-1511
    Project: CS1511
    File: blackjack-robertcurtiss
    Created: Mar, 19, 2018
    
    Description:
    
===================================================
"""
import random

from card import Card, Unprintable_Card, Positionable_Card
from hand import Hand
from deck import Deck
import games
from bj_common import BJ_Game

deck1 = Deck()

deck1.populate()

deck1.shuffle()

print(deck1)

def main():
    #pp.282
    print("Welcome to Blackjack\n")
    names = []

    number = games.ask_number("How many players (1-7): ", 1,8)
    for i in range(number):
        names.append(input("Enter Player Name: "))
        print()

    game = BJ_Game(names)

    again = None
    while again != 'n':
        game.play()
        again = games.ask_yes_no("Play again [y/n]: ")


main()

input("Press enter key to continue!")