file = open('depthNote.txt', 'r')
checkStarted = False
prev = 0
res = 0
# This will print every line one by one in the file
for each in file:
	value = int(each)
	if value > prev and checkStarted:
		res += 1
	prev = value
	checkStarted = True
print(res)