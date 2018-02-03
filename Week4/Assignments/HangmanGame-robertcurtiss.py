"""
Author: Robert W. Curtiss

Class: CSCI-1511
 -Project: CSCI1511
 -File: HangmanGame-robertcurtiss
 -Created: Feb, 02, 2018
Description:
	Hangman Game, guess the word or you are done!
"""

import random as rnd

WORDS = ["KANGAROO", "ELEPHANT", "MONGOOSE", "RACCOON", "OSTRICH", "HORSE"]
word = rnd.choice(WORDS)
# init status as a list with dashes
status = "_ " * len(word)

# make guessed letters a list
guessedLetters = []
# make word a list
wordList = list(word)
print(word)
print(status, end=" ")
# for i, j in enumerate(status):
#     print(status[i], end="")
noMatch = True
while noMatch:
    foundLetters = 0
    status = ""
    letter = input("\nYour Guess: ").upper()
    if letter in guessedLetters:
        print("You already have used that letter, try again:")
        continue
    for l in wordList:
        if letter not in guessedLetters:
            guessedLetters.append(letter)
        if l in guessedLetters :
            status += l + " "
            continue
        else:
            status += "_ "
    print(status)
    #test for exiting the loop
    if set(wordList).difference(guessedLetters) == set():
        print("You guessed it!")
        noMatch = False
# input("\nGame over Press enter to continue: ")
