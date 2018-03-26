from unittest import TestCase

__author__ = 'Robert W. Curtiss'
__project__ = 'CS1511'

"""
====================================================
Author: Robert W. Curtiss
Class: CSCI-1511
    Project: CS1511
    File: test_hand
    Created: Mar, 21, 2018
    
    Description:
    
===================================================
"""
from in_class_ex1 import Hand, Card


class TestHand(TestCase):
    def test_add(self):
        hand = Hand()
        self.assertTrue(hand.cards == [])

    def test_add2(self):
        hand = Hand()
        card1 = Card('A', 'C')
        card2 = Card('K', 'D')
        hand.add(card1)
        hand.add(card2)
        self.assertTrue(len(hand.cards) == 2)

    def test_clear(self):
        hand = Hand()
        card1 = Card('A', 'C')
        card2 = Card('K', 'D')
        hand.add(card1)
        hand.add(card2)
        hand.clear()
        self.assertTrue(len(hand.cards) == 0)

    def test_give(self):
        hand = Hand()
        card1 = Card('A', 'C')
        card2 = Card('K', 'D')
        hand.add(card1)
        hand.add(card2)
        other_hand = Hand()
        hand.give(card1, other_hand)
        self.assertTrue(len(other_hand.cards) == 1)

