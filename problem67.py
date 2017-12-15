import sys

def reduceOneLevel():
	level = len(piramid)-1
	rowtoRemove = piramid.pop(level)
	for i in range(len(piramid[level-1])) :
		piramid[level-1][i]+=max(rowtoRemove[i],rowtoRemove[i+1])

input = open("problem67.py_input","r")

piramid = dict();
i=0
for line in input :
	piramid[i] = list(map(int,line.split(" ")))
	i+=1


print("---",len(piramid),"---")
for i in range(len(piramid)):
	print(piramid[i])
while len(piramid)>1 :
	reduceOneLevel()
	print("---",len(piramid),"---")
	for i in range(len(piramid)):
		print(piramid[i])