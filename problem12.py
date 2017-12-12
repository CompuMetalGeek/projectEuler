import sys
import math

input = int(sys.argv[1])

def getDivisors(number):
	divisors = []
	for i in range(1,int(math.sqrt(number))+1):
		
		if (number % i) == 0 :
			divisors.append(i)
			if(number/i!=i):
				divisors.append(int(number/i))
	return divisors

divisors = []
triangle = 0
number = 1
while len(divisors)<input:
	triangle += number
	number += 1
	divisors = getDivisors(triangle)
	divisors.sort()
print(triangle)