"""
Author: Robert W. Curtiss

Class: CSCI-1511
 -Project: CSCI1511
 -File: fibon
 -Created: Feb, 02, 2018
Description:
http://book.pythontips.com/en/latest/generators.html
"""


def fibon(n):
	a = b = 1
	for i in range(n):
		yield a
		a, b = b, a + b


for x in fibon(1000):
	print(x)
