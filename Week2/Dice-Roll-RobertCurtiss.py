"""

Name: Robert W. Curtiss
Class: CSCI-1511
FILE: Dice-Roll-RobertCurtiss.py
Created: 1/30/2018
Project: Week2
Description: Roll the dice and sum up the points use
    an appropriate term to describe the roll!

"""

import random as rnd

rnd.seed(rnd.randint(100, 3000))
print("Welcome to Roll the Dice game!")

termsDict = {"1,1": "Snake Eyes",
             "1,2": "Ace Caught a Duce",
             "2,2": "Little Joe from Kokomo",
             "2,3": "Little Phoebe",
             "3,3": "Jimmy Hicks from the Sticks",
             "1,6": "Six Ace",
             "4,4": "Eighter from Decatur",
             "4,5": "Nina from Pasadena",
             "5,5": "Puppy Paws",
             "5,6": "Six Five no Jive",
             "6,6": "Boxcars"
             }
die = [0, 0]
rnd.seed()
while True:
    die[0] = rnd.randint(1, 6)
    die[1] = rnd.randint(1, 6)
    die.sort()
    theDots = str(die[0]) + "," + str(die[1])

    print("The roll: (%d,%d) --- Total Points: (%d)" % (die[0], die[1], die[0] + die[1]), end="")

    if theDots in termsDict:
        print(" --- (%s)" % termsDict[str(die[0]) + "," + str(die[1])])

    ans = input("\nPlay again (y): ")
    if ans == 'y':
        continue
    else:
        break
