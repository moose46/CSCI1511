"""
Author: Robert W. Curtiss

Class: CSCI-1511
 -Project: CSCI1511
 -File: finickCounter
 -Created: Jan, 31, 2018
Description:

"""

count = 0
while True:
	count += 1
	if count > 10:
		break
	if count == 5:
		continue
	print(count)
