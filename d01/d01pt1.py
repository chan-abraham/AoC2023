#d01 advent of code PT1

firstNumber = 0
secondNumber = 0
lineNumber = 0
counter = 0
sumLine = 0

f = open('txt.txt', "r")

for line in f:
	for y in line:
		if y == '1' or y == '2' or y == '3' or y == '4' or y == '5' or y == '6' or y == '7' or y == '8' or y == '9' or y == '0':
			if counter == 0:
				firstNumber = y
				secondNumber = y
				counter = 1
			if counter == 1:
				secondNumber = y
		
	counter = 0
	sumLine = sumLine + int(firstNumber)*10 + int(secondNumber)
	print(firstNumber,secondNumber)
	firstNumber = 0
	secondNumber = 0
	print(sumLine)
