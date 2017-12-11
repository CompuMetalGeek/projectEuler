import sys
import math

input = int(sys.argv[1])

for i in range(1,input):
    for j in range(i,input):
        k = i*i+j*j
        sqrtK = math.sqrt(k)
        if(sqrtK+i+j>1000):
            break
        if sqrtK==int(sqrtK) :
            if i+j+sqrtK==input :
                print(i,j,int(sqrtK),int(i*j*sqrtK))
                sys.exit(0)
