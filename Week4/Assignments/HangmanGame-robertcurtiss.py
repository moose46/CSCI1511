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

#init status as a list with dashes
status = ["_ "] * len(word)

#make guessed letters a list
guessedLetters = []
#make word a list
wordList = list(word)
print(word)
for i,j in enumerate(status):
	print(status[i],end="")
while True:
	letter = input("\nYour Guess: ").upper()
	if letter in guessedLetters:
		print("You already have used that letter, try again:")
		continue
	for i, j in enumerate(wordList):
		if j == letter:
			guessedLetters.append(letter)
	for i, j in enumerate(status):
		if wordList[i] == letter:
			status[i] = letter + " "
			continue
		if letter in guessedLetters and letter == j:
			status[i] += letter + " "
	for i, j in enumerate(status):
		print(status[i], end="")
# print(guessedLetters)o

# input("\nPress enter to continue: ")
