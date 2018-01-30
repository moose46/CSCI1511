"""

Name: Robert W. Curtiss
Class: CSCI-1511
FILE: guessNumber-robertcurtiss
Created: 1/30/2018
Project: Week2
Description:

"""
import random as rnd

print("""\nThis game will pick a random number and you will try to guess it.
I will let you know if you are too high or too low,
and if you have the correct number.
Lets go!""")

theNumber = rnd.randint(1, 100)
yourNumber = -1
numberOfTries = 0
while yourNumber != theNumber:

    while True:
        try:
            yourNumber = int(input("Pick a number between (1-100): "))
            break
        except Exception as ex:
            print("\nNumbers only please, try again!\n")
            continue

    if yourNumber == theNumber:
        break
    elif yourNumber > theNumber:
        print("\n%s is too high!" % yourNumber)
    elif yourNumber < theNumber:
        print("\n%s is too low!\n" % yourNumber)
    numberOfTries += 1
print("\nCongratulation's, the number was indeed %s" % theNumber)
print("\nIt took you %s tries!\n" % numberOfTries)

input("Press enter to continue!")
