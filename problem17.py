import sys

def getText(input):
	text = ""
	initialLen = len(input)
	if len(input) == 4:
		input.pop(0)
		text += "onethousand"
	if len(input) == 3:
		number = int(input.pop(0))
		text += numerals[number]
		if number != 0 :
			text += "hundred"
	try:
		if initialLen>2 and not (input[0]=="0" and input[1]=="0") :
			text+="and"
	except :
		pass
	if len(input) == 2:
		number = int(input.pop(0)) * 10
		if number == 10 :
			number += int(input.pop(0))
		text += numerals[number]
	if len(input) == 1 :
		number = int(input.pop(0))
		text+= numerals[number]
	return text

numerals = { 0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 
			6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 
			11: "eleven", 12:"twelve", 13:"thirteen", 14: "fourteen", 
			15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 
			19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 
			50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety" }
sum = 0
for number in range(int(sys.argv[1]),int(sys.argv[2])):
	word = getText(list(str(number)))
	sum += len(word)
	print(word)
print(sum)
