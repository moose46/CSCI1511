"""
Author: Robert W. Curtiss

Class: CSCI-1511
 -Project: CSCI1511
 -File: DealEm-robertcurtiss
 -Created: Jan, 31, 2018
Description:
    Asks the user for the number of players and the number of cards in each hand.
    Then, displays all hands of cards from a deck of playing cards
    using the same format as described in Project 3.

"""
import random as rnd

# init the deck of cards
suits = ["Hearts", "Clubs", "Diamonds", "Spades"]
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
deck = []
# create the deck of cards with all four suits
for suit in suits:
	for card in cards:
		deck.append((card, suit))

thePile = list(deck)

#loop through all cards, and remove them from the pile one at a time
for card in deck:
	i = rnd.randint(0, len(thePile) - 1)
	oneCard = thePile.pop(i)

print(deck)
# print("{0} of {1}\n".format(oneCard[0], oneCard[1]))
#print("\nPress enter to continue: ")
