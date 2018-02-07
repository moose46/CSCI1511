"""
Author: Robert W. Curtiss

Class: CSCI-1511
 -Project: CSCI1511
 -File: find-upc-robertcurtiss.com
 -Created: Feb, 06, 2018
Description:
Returns a check digit to determine if it is a valid upc
http://wikipedia.org/wiki/Universal_Product_code
(3x1 + x2 + 3x3 + x4 + 3x5 + x6 + 3x7 + x8 + 3x9 + x10 + 3x11 + x12) === (mod 10)
"""

SystemNumberDigit = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
ValidDigits = [str(num) for num in range(0, 10)]
UPC_LEN = 12
CONDITIONS = ["Good", "Incorrect"]


def systemMessage(message, upc):
	""" Display error message """
	print("\t\t", upc, " -> ", message)


def checkNumericalDigits(upc):
	""" Check for valid upc conditions """
	for i in upc:
		if i not in ValidDigits:
			systemMessage("Invalid digit (" + i + ")", upc)
			return CONDITIONS[1]
	if len(upc) != UPC_LEN:
		systemMessage('Incorrect length', upc)
		return CONDITIONS[1]
	return calculateCheckNumber(upc)


def calculateCheckNumber(upc):
	sumOddNumbers = 0
	sumEvenNumbers = 0
	oddNumbers = []
	evenNumbers = []
	x = 0
	while x < 12:  # sum the odd positions first, third ...
		sumOddNumbers += int(upc[x])
		oddNumbers.append(upc[x])
		x += 2
	x = 1
	while x < 11:
		sumEvenNumbers += int(upc[x])
		evenNumbers.append(upc[x])
		x += 2
	oddNumbersResult = sumOddNumbers * 3
	modulo = (sumEvenNumbers + oddNumbersResult) % 10
	theCheckNumber = 0
	if modulo != 0:
		theCheckNumber = 10 - modulo
	# print(theCheckNumber)
	if theCheckNumber == int(upc[11]):
		systemMessage("Passed!", upc)
		return True
	else:
		systemMessage("Checksum failed digit (" + upc[11] + ")", upc)
		return False


def getUPC(question):
	pass


def printInstructions():
	pass


checkUPCS = [
	"708163125126",  # chips good number
	"708163125116",  # chips sum bad
	"712375678999",  # check sum bad
	"1234566789",  # short
	"2345ABC12333",  # has a character
	"036000291452",
	"036000291457",
	"082039555003",
	"073999650181"  # music book
]
print("Sample inputs:")

for upc in checkUPCS:
	checkNumericalDigits(upc)

print("Now you try, press enter to exit\n")
yourUPC = ""
while True:
	yourUPC = input("Enter the UPC code: ")
	if len(yourUPC) == 0:
		break
	checkNumericalDigits(yourUPC)
