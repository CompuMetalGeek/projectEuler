import sys
import math

maximum = int(sys.argv[1])
sum=0
squareSum=0
for i in range(1,maximum+1):
    sum +=i
    squareSum+=i*i
sumSquared=sum*sum
print(sumSquared,"-",squareSum,"=",sumSquared-squareSum)