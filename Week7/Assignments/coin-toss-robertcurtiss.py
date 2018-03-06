"""
====================================================
Author: Robert W. Curtiss
Class: CSCI-1511
    Project: CS1511
    File: coin-toss-robertcurtiss
    Created: Mar, 06, 2018
    
    Description:
    
===================================================
"""
from coin import Coin


def print_status(player1, player2):
    print("Player 1 Balance: ", player1.get_amount())
    print("Player 2 Balance: ", player2.get_amount())


def main():
    player1 = Coin()
    player2 = Coin()
    choice = 'y'
    while choice == 'y':
        print("====================================")
        print_status(player1, player2)
        print("====================================")
        choice = input("\nDo want to continue [Y/y]? ").lower()
        if choice != 'y':
            break
        player1.toss()
        player2.toss()
        if player1.get_side_up() == player2.get_side_up():
            player1.add_one()
            player2.take_one()
            print("\n\nPlayer one wins, they match [{}/{}]".format(player1.get_side_up(), player2.get_side_up()))
        else:
            player1.take_one()
            player2.add_one()
            print("\n\nPlayer two wins, they do not match [{}/{}]".format(player1.get_side_up(), player2.get_side_up()))


main()
