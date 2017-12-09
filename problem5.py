import sys
import math

maximum = int(sys.argv[1])
factors = []

def generateFactors(number):
    factors =[]
    for prime in range(2,number+1):
        if number==1:
            break
        while number%prime==0:
            factors.append(prime)
            number/=prime
    return factors


numbers = range(2,maximum+1)
allFactors = []
for i in numbers:
    factors = generateFactors(i)
    for factor in factors:
        while factors.count(factor) > allFactors.count(factor):
            allFactors.append(factor)
lcm = 1
for i in allFactors:
    lcm*=i
print(lcm)