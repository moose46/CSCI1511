"""
Author: Robert W. Curtiss

Class: CSCI-1511
 -Project: CSCI1511
 -File: WordJumble-robertcurtiss.com
 -Created: Jan, 31, 2018
Description:
    The computer picks a random word and then jumbles it.
    The player has to guess the original word
"""

import random as rnd

WORDS = ("water", "snow", "ice", "river", "lake", "pond")

randomWord = rnd.choice(WORDS)
# save the original word for later
savedWord = randomWord
jumbledWord = ""
score = 100

while randomWord:
	position = rnd.randrange(len(randomWord))
	jumbledWord += randomWord[position]
	randomWord = randomWord[:position] + randomWord[(position + 1):]

print("""\tWelcome to the world of jumble!
\tUnscramble the letter to make a word:\n""")

print("%s %s" % (savedWord, jumbledWord))

guess = input("Your guess: ")
while guess != savedWord and guess != "":
	hint = ""
	print("Sorry that's not correct!")
	hint = input("Would you like a hint? [y]: ")
	if hint != "":
		positionHint = rnd.randrange(len(savedWord))
		print("Word Letter [%s] is an %s " % (positionHint + 1, savedWord[positionHint]))
	guess = input("Your guess: ")
	score -= 1

print("You guessed it, congratulations!")
print("Thanks for playing!")
input("\n\nPress enter to exit:")
