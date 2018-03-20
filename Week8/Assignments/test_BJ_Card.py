from unittest import TestCase

__author__ = 'Robert W. Curtiss'
__project__ = 'CS1511'

"""
====================================================
Author: Robert W. Curtiss
Class: CSCI-1511
    Project: CS1511
    File: test_BJ_Card
    Created: Mar, 19, 2018
    
    Description:
    
===================================================
"""

from bj_common import BJ_Card

class TestBJ_Card(TestCase):
    def test_value(self):
        card = BJ_Card(rank=BJ_Card.RANKS[0], suit=BJ_Card.SUITS[0])
        #ace of hearts = 1
        self.assertTrue(card.value == 1)

