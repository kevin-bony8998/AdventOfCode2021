from collections import deque

file = open('depthNote.txt', 'r')
prevTotal = 0
currTotal = 0
queue = deque()
res = 0
for each in file:
	value = int(each)
	queue.append(value)
	currTotal += value
	if len(queue) == 3:
		prevTotal = currTotal
	if len(queue) > 3:
		checkStarted = True
		poppedVal = queue.popleft()
		currTotal -= poppedVal
		if currTotal > prevTotal: 
			res += 1
		prevTotal = currTotal

print(res)