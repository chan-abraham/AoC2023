#d01 advent of code PT2

firstNumber = 0
secondNumber = 0
lineNumber = 0
counter = 0
sumLine = 0
indexFirstnumber = 0
indexSecondnumber = 0
indexWord = 0
x = 0

f = open('txt.txt', "r")

for line in f:
	for y in line:
		if y == '1' or y == '2' or y == '3' or y == '4' or y == '5' or y == '6' or y == '7' or y == '8' or y == '9' or y == '0':
			if counter == 0:
				firstNumber = y
				secondNumber = y
				counter = 1
				indexFirstnumber = line.find(y)
			if counter == 1:
				secondNumber = y
				indexSecondnumber = line.rfind(y)


##first block to find words before first index number
	x = line.find('zero', 0, indexFirstnumber + 4)
	if x != -1:
		firstNumber = 0
		indexFirstnumber = x
	x = line.find('one', 0, indexFirstnumber + 3)
	if x != -1:
		firstNumber = 1
		indexFirstnumber = x
	x = line.find('two', 0, indexFirstnumber + 3)
	if x != -1:
		firstNumber = 2
		indexFirstnumber = x
	x = line.find('three', 0, indexFirstnumber + 5)
	if x != -1:
		firstNumber = 3
		indexFirstnumber = x
	x = line.find('four', 0, indexFirstnumber + 4)
	if x != -1:
		firstNumber = 4
		indexFirstnumber = x
	x = line.find('five', 0, indexFirstnumber + 4)
	if x != -1:
		firstNumber = 5
		indexFirstnumber = x
	x = line.find('six', 0, indexFirstnumber + 3)
	if x != -1:
		firstNumber = 6
		indexFirstnumber = x
	x = line.find('seven', 0, indexFirstnumber + 5)
	if x != -1:
		firstNumber = 7
		indexFirstnumber = x
	x = line.find('eight', 0, indexFirstnumber + 5)
	if x != -1:
		firstNumber = 8
		indexFirstnumber = x
	x = line.find('nine', 0, indexFirstnumber + 4)
	if x != -1:
		firstNumber = 9
		indexFirstnumber = x
		print('1')

	##2nd block to find words ending
	z = line.rfind('zero', indexSecondnumber)
	if z != -1:
		secondNumber = 0
		indexSecondnumber = z 
	z = line.rfind('one', indexSecondnumber)
	if z != -1:
		secondNumber = 1
		indexSecondnumber = z 
	z = line.rfind('two', indexSecondnumber)
	if z != -1:
		secondNumber = 2
		indexSecondnumber = z 
	z = line.rfind('three', indexSecondnumber)
	if z != -1:
		secondNumber = 3
		indexSecondnumber = z 
	z = line.rfind('four', indexSecondnumber)
	if z != -1:
		secondNumber = 4
		indexSecondnumber = z 
	z = line.rfind('five', indexSecondnumber)
	if z != -1:
		secondNumber = 5
		indexSecondnumber = z 
	z = line.rfind('six', indexSecondnumber)
	if z != -1:
		secondNumber = 6
		indexSecondnumber = z 
	z = line.rfind('seven', indexSecondnumber)
	if z != -1:
		secondNumber = 7
		indexSecondnumber = z 
	z = line.rfind('eight', indexSecondnumber)
	if z != -1:
		secondNumber = 8
		indexSecondnumber = z 
	z = line.rfind('nine', indexSecondnumber)
	if z != -1:
		secondNumber = 9
		indexSecondnumber = z 

	x = 0
	counter = 0
	sumLine = sumLine + int(firstNumber)*10 + int(secondNumber)
	print(firstNumber,secondNumber)
	firstNumber = 0
	secondNumber = 0
	indexFirstnumber = 0
	indexSecondnumber = 0


print(sumLine)