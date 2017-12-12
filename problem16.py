import sys
import math

input = int(sys.argv[1])

numbers = [1]

def numbersToString():
	string = ""
	for number in numbers:
		string += str(number)
	return string

power = 0
rememberOne = 0
while power < input :
	for i in range(len(numbers)-1,-1,-1) :
		new = numbers[i] * 2
		if rememberOne == 1 :
			new += 1
			rememberOne = 0
		if 9 < new :
			rememberOne = 1
			new-=10
		numbers[i] = new
	if rememberOne == 1 :
		numbers = [1] + numbers
		rememberOne = 0
	power+=1


print("2**%d: %s" % (power,numbersToString()))
print(sum(numbers))