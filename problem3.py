import sys
import math

number = int(sys.argv[1])
factors = []
print(int(math.sqrt(number)))
for prime in range(2,int(math.sqrt(number))):
    if number==1:
        break
    while number%prime==0:
        factors.append(prime)
        number/=prime

print(factors)