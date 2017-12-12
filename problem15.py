import sys
import math

input = int(sys.argv[1])*2


print(int(math.factorial(input)/(math.factorial(int(input/2))*math.factorial(int(input/2)))))