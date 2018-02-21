"""
Author: Robert W. Curtiss

Class: CSCI-1511
 -Project: CSCI1511
 -File: selection-sort-robertcurtiss
 -Created: Feb, 04, 2018
Description: Selection sort on an unordered list

"""

import  random as rnd

unOrderd = list(range(20))

ordered = []

rnd.shuffle(unOrderd)

print(unOrderd)


print("Sorts unordered list of integers\n\n")
while len(unOrderd) > 0:
	lowest = unOrderd[0]
	for num in unOrderd:
		if num <= lowest:
			lowest = num
	unOrderd.remove(lowest)
	ordered.append(lowest)

print(ordered)

input("\nPress enter to continue: ")


