__author__ = 'Robert W. Curtiss'
__project__ = 'CS1511'

"""
====================================================
Author: Robert W. Curtiss
Class: CSCI-1511
    Project: CS1511
    File: hand
    Created: Mar, 19, 2018
    
    Description:
    
===================================================
"""
class Hand(object):

    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + " "
        else:
            rep = "<empty>"
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        """
        pp.272, 253,254
        :param card: removes card from the card list
        :param other_hand: add a card to the other hand
        :return:
        """
        self.cards.remove(card)
        other_hand.add(card)
