__author__ = 'Robert W. Curtiss'
__project__ = 'CS1511'

"""
====================================================
Author: Robert W. Curtiss
Class: CSCI-1511
    Project: CS1511
    File: deck
    Created: Mar, 19, 2018
    
    Description:
    
===================================================
"""
from hand import Hand
from card import Card
import random


class Deck(Hand):
    """
        pp.272
    """
    def populate(self):
        """

        :return: None
        """
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):
        """

        :return: None
        """
        random.shuffle(self.cards)

    def deal(self, hands, per_hand=1):
        """
        pp.272
        :param hands: list of players
        :param per_hand: number of cards to deal to each player
        :return:
        """
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Can't continue deal, out of cards")
