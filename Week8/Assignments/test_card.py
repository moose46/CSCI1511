from unittest import TestCase

__author__ = 'Robert W. Curtiss'
__project__ = 'CS1511'

"""
====================================================
Author: Robert W. Curtiss
Class: CSCI-1511
    Project: CS1511
    File: test_card
    Created: Mar, 19, 2018
    
    Description:
    
===================================================
"""

from card import Card

class TestCard(TestCase):
    def test_flip(self):
        card = Card(rank=Card.RANKS[0], suit=Card.SUITS[0])
        card.flip()

        self.assertFalse(card.is_face_up)

