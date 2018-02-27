"""
Author: Robert W. Curtiss

Class: CSCI-1511
 -Project: CSCI1511
 -File: trivia-challenge-robertcurtiss
 -Created: Feb, 07, 2018
Description:
Tests a players knowledge with a series of multiple questions
"""

import sys


def openTheTriviaFile(filename, mode):
    """Opens the trivial file and returns the file"""
    try:
        theFile = open(filename, mode)
    except Exception as Ex:
        print("Unable to open file: ", Ex)
        input("\nPress enter to continue: ")
        sys.exit()
    else:
        return theFile


def nextLine(theFile):
    """return the next trivia line all formatted"""
    line = theFile.readline()
    line = line.replace("/", "\n")
    return line


def nextBlock(theFile):
    """return the next block of the trivia file"""
    category = nextLine(theFile)
    question = nextLine(theFile)
    answers = []
    for i in range(4):
        answers.append(nextLine(theFile))
    correct = nextLine(theFile).replace("\n", "")
    explanation = nextLine(theFile)
    return category, question, answers, correct, explanation


def welcome(title):
    """Announces the game and it's instructions and gets their name"""
    print("\t\tWelcome to the trivia game.\n\n")
    print("\t\t", title)
    score = 0
    while True:
        try:
            name = input("Enter your name please: ").capitalize()
            print("Welcome ", name)
            break
        except Exception as Ex:
            print("Input error, try again!")
            continue
    return name


def main():
    name = ""
    theFile = openTheTriviaFile("trivia-1-robertcurtiss.txt", "r")
    title = nextLine(theFile)
    name = welcome(title)
    score = 0
    category, question, answers, correct, explanation = nextBlock(theFile)  # with open(

    while category:

        print("==========================================")
        print(category)
        print(question)
        print("==========================================")
        for i in enumerate(answers):
            print("\t", i[0] + 1, i[1], end="")
        print("\t\n", name, end="")
        answer = input(" what's your answer?: ")

        # check answer
        if answer == correct:
            print("\n\tCorrect!", end=' ')
            score += 1
        else:
            print("\n\tWrong!", end=" ")
        print(explanation)
        print("\tYour Score:", score, "\n")

        # get next block
        category, question, answers, correct, explanation = nextBlock(theFile)  # with open(


main()
# "trivia-1-robertcurtiss.txt","r") as f:
# 	data = f.readlines()
#
# for i, line in enumerate(data):
# 	print(i, line)
# print(textFile.read())

# for lines in data:
# 	print(lines, end='')

openTheTriviaFile("trivia-1-robertcurtiss.txt", "r")
