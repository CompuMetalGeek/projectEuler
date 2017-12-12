import sys
import math

input = int(sys.argv[1])

def collatzLength(number):
	length=1
	while number != 1 :
		if number % 2 == 0 :
			number/=2
		else :
			number*=3
			number+=1
		length+=1
	return length

max = 0
number = 0
for i in range(1,input,2):
	if(i%10000==1):
		print(i)
	length = collatzLength(i)
	if max < length :
		max = length
		number = i
print("%d :%d" % (number,max)) 