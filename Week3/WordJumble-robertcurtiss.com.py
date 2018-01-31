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

while randomWord:
    position = rnd.randrange(len(randomWord))
    jumbledWord += randomWord[position]
    randomWord = randomWord[:position] + randomWord[(position + 1):]

print("""\tWelcome to the world of jumble!
\tUnscramble the letter to make a word:\n""")


print("%s %s" % (savedWord, jumbledWord))

guess = input("Your guess: ")
while guess != savedWord and guess != "":
    print("Sorry that's not correct!")
    guess = input("Your guess: ")

print("You guessed it, congratulations!")
print("Thanks for playing!")
# input("Press enter to exit:")
