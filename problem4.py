import sys
import re

number = int(sys.argv[1])
palindromes = []
i=number
j=number

for i in range(number,1,-1):
    for j in range(i,1,-1):
        palindrome = repr(i*j)
        if palindrome == palindrome[::-1]:
            palindromes.append(palindrome)

print(sorted(palindromes,key=int,reverse=True)[0])