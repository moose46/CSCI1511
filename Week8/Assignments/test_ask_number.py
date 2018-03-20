from unittest import TestCase

__author__ = 'Robert W. Curtiss'
__project__ = 'CS1511'

"""
====================================================
Author: Robert W. Curtiss
Class: CSCI-1511
    Project: CS1511
    File: test_ask_number
    Created: Mar, 19, 2018
    
    Description:
    
===================================================
"""

import games
class TestAsk_number(TestCase):
    def test_ask_number(self):
        response = games.ask_number(question="Enter # [1-7]: ", low=1,high=8)
        self.assertTrue(response >= 1 and response <= 7)

