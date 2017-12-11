import sys
import math
from datetime import datetime

if len(sys.argv) < 3:
	print("Error: missing argument(s)\nusage: 'python",sys.argv[0]," $index, $step'")
	sys.exit(0)
try:
	input = int(sys.argv[1])-1
	step = int(sys.argv[2])
except ValueError:
	print("Arguments must be decimal integer values, instead received '%s' and '%s'" % (sys.argv[1],sys.argv[2]))
	sys.exit(0)

primes = [2,3,5,7]

def generatePrimesSmallerThan(limit):
	print("Generating all primes smaller than %8d " % limit, end='')
	time = datetime.today()
	numbers = list(range(limit-step,limit))
	for prime in primes:
		i=0
		while i < len(numbers):
			if numbers[i]%prime==0:
				numbers.pop(i)
			else:
				i+=1
	while 0<len(numbers):
		primes.append(numbers.pop(0))
		if primes[-1]==1 :
			primes.pop(-1)
			continue
		toRemove = primes[-1]
		while(toRemove<limit):
			try:
				numbers.remove(toRemove)
			except:
				pass
			toRemove += primes[-1]
	print("(%.3f s elapsed)" % (datetime.today()-time).total_seconds())

currentLimit=step
while primes[-1]<input:
	generatePrimesSmallerThan(currentLimit)
	currentLimit+=step

print(sum(primes[i] for i in range(len(primes)) if primes[i]<input))