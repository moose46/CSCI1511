__author__ = 'Robert W. Curtiss'
__project__ = 'CS1511'

"""
====================================================
Author: Robert W. Curtiss
Class: CSCI-1511
    Project: CS1511
    File: Card
    Created: Mar, 19, 2018
    
    Description:
    
===================================================
"""


class Card(object):
    # init the deck of cards
    SUITS = ["Hearts", "Clubs", "Diamonds", "Spades"]
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, rank, suit, face_up=True):
        self.rank = rank
        self.suit = suit
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = self.rank + '-' + self.suit
        else:
            rep = 'XX'
        return rep

    def flip(self):
        self.is_face_up = not self.is_face_up


class Unprintable_Card(Card):
    def __str__(self):
        return "<unprintable>"


class Positionable_Card(Card):
    def __init__(self, rank, suit, face_up=True):
        super(Positionable_Card, self).init(rank, suit)
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            super(Positionable_Card, self).__str__()
        else:
            return 'XX'

    def flip(self):
        self.is_face_up = not self.is_face_up
