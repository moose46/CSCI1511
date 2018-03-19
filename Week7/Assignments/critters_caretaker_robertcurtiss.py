"""
====================================================
Author: Robert W. Curtiss
Class: CSCI-1511
    Project: CS1511
    File: critters-caretacker-robertcurtiss
    Created: Mar, 06, 2018
    
    Description:
    
===================================================
"""

from critter import Critter
def main():
    crit_name = input("What is the name of your critter going to be? ")
    crit = Critter(crit_name)

    choice = None

    while choice != "0":
        print("""
        Critter Caretaker
        
        0 = Quit
        1 - Listen to your critter
        2 - Feed your critter
        3 - Play with your critter""")
        choice = input("Enter your choice please: ")
        #exit
        if choice == "0":
            print("Goodbye")
        elif choice == "1":
            crit.talk()
        elif choice == "2":
            crit.eat()
        elif choice == '3':
            crit.play()
        else:
            print("Choice not found!\n")

main()

input("Press enter to continue\n")
