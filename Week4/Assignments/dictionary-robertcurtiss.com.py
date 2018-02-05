"""
Author: Robert W. Curtiss

Class: CSCI-1511
 -Project: CSCI1511
 -File: dictionary-robertcurtiss.com
 -Created: Feb, 05, 2018
Description:
Find animals, people, or plants, by entering the correct menu item selection
"""

theDict = {"people":  ["Nick Foles",
					   "Eddie George",
					   "Tom Brady",
					   "Walter Payton (Sweetness)"],
		   "animals": ["Dog",
					   "Cat",
					   "Bird",
					   "Raccoon",
					   "Possum"],
		   "plants":  ["Poison Ivy",
					   "Sunflower",
					   "Tomato",
					   "Grass"]}

theItems = []
while True:
	print("""\t0 - Quit
	1 - Plants
	2 - People
	3 - Animals""")
	selection = input("Please Enter A Choice [0-3]: ")
	if selection == "0":
		break
	elif selection == "1":
		theItems = theDict["plants"]
	elif selection == "2":
		theItems = theDict["people"]
	elif selection == "3":
		theItems = theDict["animals"]
	print("\n[ ", end="\t")
	for item in theItems:
		print(item, end="  ")
	print(" ]\n")