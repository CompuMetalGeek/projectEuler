import sys
sum=0
current=1
previous=0
preprevious=0
while current<int(sys.argv[1]):
    print(current)
    if current%2==0:
        sum+=current
    preprevious=previous
    previous=current
    current=previous+preprevious
print(sum)
