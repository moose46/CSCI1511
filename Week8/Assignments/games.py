__author__ = 'Robert W. Curtiss'
__project__ = 'CS1511'

"""
====================================================
Author: Robert W. Curtiss
Class: CSCI-1511
    Project: CS1511
    File: games
    Created: Mar, 19, 2018
    
    Description:
    
===================================================
"""


class Player(object):
    """a player for the bj game"""

    def __init__(self, name, score=0):
        self.name = name
        self.score = score

    def __str__(self):
        return self.name + "\t" + self.score


def ask_yes_no(question):
    response = None
    while response not in ('y', 'n'):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    """
    pp.269
    :param question:
    :param low:
    :param high:
    :return: Number
    """
    response = None
    while response not in range(low, high):
        response = int(input(question).lower())
    return response


if __name__ == "__main__":
    print('You ran this module directly, and did not import it')
    input('Press enter to continue: ')
