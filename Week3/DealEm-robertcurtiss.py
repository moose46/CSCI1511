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

# init the deck of cards
suits = ["Hearts", "Clubs", "Diamonds", "Spades"]
cards = []

# create the deck of cards with all four suits
for suit in suits:
	cards.append([(1, "1 ", suit),
				  (2, "2 ", suit),
				  (3, "3 ", suit),
				  (4, "4 ", suit),
				  (5, "5 ", suit),
				  (6, "6 ", suit),
				  (7, "7 ", suit),
				  (8, "8 ", suit),
				  (9, "9 ", suit),
				  (10, "10 ", suit),
				  (10, "J ", suit),
				  (10, "Q ", suit),
				  (10, "K ", suit),
				  (11, "A ", suit)])

for suit in cards:
	for card in suit:
		print(card[1],card[2])

print("\nPress enter to continue: ")
