__author__ = 'Robert W. Curtiss'
__project__ = 'CS1511'

"""
====================================================
Author: Robert W. Curtiss
Class: CSCI-1511
    Project: CS1511
    File: in_class_ex1
    Created: Mar, 21, 2018
    
    Description:
    
===================================================
"""


class Card(object):
    # init the deck of cards pp.257
    SUITS = ["Hearts", "Clubs", "Diamonds", "Spades"]
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return "{}{}".format(self.rank, self.suit)


class Hand(object):
    cards = []
    def __init__(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def clear(self):
        self.cards = []

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

    def __str__(self):
        rep = ''
        if self.cards:
            for card in self.cards:
                rep += str(card) + '\t'
        else:
            return "<empty>"
        return rep


card1 = Card('A','c')
print("printing card1\n")
print(card1)

card2 = Card('2','c')
card3 = Card('3','c')
card4 = Card('4','c')
card5 = Card('5','c')

print('Rest of cards, one by one')
print(card2)
print(card3)
print(card4)
print(card5)


my_hand = Hand()
print('My hand before I add any cards')
print(my_hand)

print('Added some cards to the deck')
my_hand.add(card1)
my_hand.add(card2)

print(my_hand)






