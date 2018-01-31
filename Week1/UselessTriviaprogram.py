# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 19:03:00 2018

@author: Robert Curtiss
Week 2: Lab 1
Description: The Useless Trivia Program, gets user input

    
"""
# Globals
age = 0.0
weight = 0

# Start here.......
print("""\nWelcome to my useless trivia program.
      Really it is useless!
      Good Luck!!\n\n""")

name = input("Enter your name to get started: ")
print("Hello {0}".format(name))
while True:
    try:
        age = float(input("How old are you?: "))
        break
    except Exception as Ex:
        print("Numbers only please!")
        continue

while True:
    try:
        weight = int(input("How much to you weigh?: "))
        break
    except Exception as Ex:
        print("Numbers only please!")
        continue

# Display useless trivia
print("\nOn the moon {1} would weigh ~ {0} pounds, and you are over  {2:,.2f} seconds old!".format(weight // 6,
                                                                                                   name.capitalize() * 5,
                                                                                                   age * 365 * 24 * 60 * 60))

print("On the sun you would weigh {0} pounds, not for long though!\n".format(int(weight * 27.1)))
# display more trivia
print("""=========================================
\nBonus Trivia:\n
If cheese gets it picture taken, what does it say?
If a turtle loses it’s shell is he homeless, naked or both?
Can a vegetarian eat animal crackers?
What happens if a black cat carrying a rabbit’s foot crosses your path?
=================================================""")
input("\nPress Enter to continue...")

# Soo long, goodbye and thanks for all the fish
