# -*- coding: utf-8 -*-
"""

CSCI-1511

Created on Mon Jan 29 15:51:31 2018

@author: Robert Curtiss

Description: Car Salesman Program
User enters base price of te car, 
the program prints out all the extra fees,
such as tax, dealer fees, tax, license, etc,
along with the final price.
    
"""
# init variables
base_price = 0.0
tax_fee = .18
dealer_prep = 100.0
license_fee = .05
actual_price = 0.0
delivery_fee = 100.0
while True:
    try:
        base_price = float(input("\nEnter Base Price: "))
        break
    except Exception as ex:
        print("Please use numbers only, try again: ")
        continue
print("\n\nDealer Invoice-----------------------------------\n")
print("Base Price:\t\t ${0:,.2f}".format(base_price))
print("Tax ({1:n}%):\t\t ${0:,.2f}".format(base_price * tax_fee, tax_fee * 100))
actual_price += base_price + tax_fee * base_price
print("Dealer Prep:\t ${0:,.2f}".format(dealer_prep))
actual_price += dealer_prep
print("License ({1:n}%):\t ${0:,.2f}".format(base_price * license_fee, license_fee * 100))
actual_price += base_price * license_fee
print("Delivery Fee:\t ${0:,.2f}".format(delivery_fee))
actual_price += delivery_fee
print("Actual Price:\t ${0:,.2f}".format(actual_price))

input("\nPress Enter to continue...")
