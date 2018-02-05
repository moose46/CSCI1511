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
import HangmanGlyphs as glyphs



WORDS = ["KANGAROO", "ELEPHANT", "MONGOOSE", "RACCOON", "OSTRICH", "HORSE"]
word = rnd.choice(WORDS)
# init status as a list with dashes
status = "_ " * len(word)
correctGuesses = 0
inCorrectGuesses = 0
numberOfGuesses = 0
max_tries = 8
# make guessed letters a list
guessedLetters = []
# make word a list
wordList = list(word)
#print(word)
print(status)

noMatch = True
while noMatch:
	foundLetters = 0
	status = ""
	#print(inCorrectGuesses)
	print(glyphs.man[inCorrectGuesses])
	numberOfGuesses += 1
	if inCorrectGuesses == len(glyphs.man) - 1:
		print(" ----- You are a goner!")
		noMatch = False
		continue
	#
	letter = input("\nYour Guess: ").upper()
	if letter in guessedLetters:
		print("You already have used that letter, try again:")
		continue
	if letter not in wordList:
		inCorrectGuesses += 1
	for l in wordList:
		if letter not in guessedLetters:
			guessedLetters.append(letter)
		if l in guessedLetters:
			status += l + " "
			correctGuesses += 1
			continue
		else:
			status += "_ "
	print(status, end='')
	# test for exiting the loop
	if set(wordList).difference(guessedLetters) == set():
		print(" ---- You guessed it!")
		noMatch = False
input("\nGame over Press enter to continue: ")
