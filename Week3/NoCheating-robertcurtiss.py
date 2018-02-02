"""
Author: Robert W. Curtiss

Class: CSCI-1511
 -Project: CSCI1511
 -File: NoCheating-robertcurtiss
 -Created: Feb, 02, 2018
Description: 4. CHALLANGE WEEK 3
Makes sure that no cards are duplicated

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
players = []
numberOfPlayers = 0
while True:
	try:
		numberOfPlayers = int(input("Enter the number of players [1-5]: "))
		if numberOfPlayers > 5 or numberOfPlayers < 1:
			print("Not an acceptable value [1-5], try again!")
			continue
		break
	except Exception as ex:
		print("Numbers only :(!\n")
		continue
for p in range(1, numberOfPlayers + 1):
	players.append("Player " + str(p))
# assign each player the cards and remove them from the pile one at a time
for player in players:
	# deal 5 cards to each player
	playersHand = []
	for dealCard in range(0, 5):
		i = rnd.randint(0, len(thePile) - 1)
		playersHand.append(thePile.pop(i))
	print("\n{0} Hand is:".format(player))
	cardNumber = 0
	playersHand.sort()
	for card in playersHand:
		print("\t{0} of {1} ".format(card[0], card[1]))

input("\nPress enter to continue: ")
