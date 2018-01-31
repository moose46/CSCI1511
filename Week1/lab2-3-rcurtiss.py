# -*- coding: utf-8 -*-
"""

CSCI-1511

Created on Mon Jan 29 13:59:57 2018

@author: Robert Curtiss

Description: User enters a restaurant bill total. The program
displays two amounts:
            15 percent tip
            20 percent tip
    
"""
bill_total = 0.0
print("\nWelcome to the tipper tip program\n")
while True:
    try:
        bill_total = float(input("Please enter the restaurant bill total: "))
        break
    except Exception as ex:
        print("We only accept numbers in the program, try again:\n")
        continue

print("You entered ${0:,.2f}".format(bill_total))
print("A 15% tip would be ${0:,.2f}".format(bill_total * .15))
print("A 20% tip would be ${0:,.2f}".format(bill_total * .20))

input("\nPress Enter to continue...")
