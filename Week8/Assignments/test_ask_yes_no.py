from unittest import TestCase

__author__ = 'Robert W. Curtiss'
__project__ = 'CS1511'

"""
====================================================
Author: Robert W. Curtiss
Class: CSCI-1511
    Project: CS1511
    File: test_ask_yes_no
    Created: Mar, 19, 2018
    
    Description:
    
===================================================
"""

import games
class TestAsk_yes_no(TestCase):
    def test_ask_yes_no(self):
        response = games.ask_yes_no("Enter [y/n]")
        self.assertIsNotNone(response)
