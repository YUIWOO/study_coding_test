def insert(value):
	max_heaps[0] +=1
	idx = max_heaps[0]
	if len(max_heaps) <= max_heaps[0]:
		max_heaps.append(0)
	while idx != 1 and value > max_heaps[idx//2]:
		max_heaps[idx] = max_heaps[idx//2]
		idx //=2
	max_heaps[idx] = value

def delete():
	if max_heaps[0] == 0:
		return 0
	value = max_heaps[1]
	max_heaps[0]-=1
	size = max_heaps[0]
	temp = max_heaps[size + 1]
	parent = 1
	child = 2
	while child <= size:
		if child < size and max_heaps[child] < max_heaps[child + 1]:
			child+=1
		if temp >= max_heaps[child]:
			break
		max_heaps[parent] = max_heaps[child]
		parent = child
		child *=2
	max_heaps[parent] = temp
	return value

import sys
input = sys.stdin.readline
n = int(input())
max_heaps = [0]
for i in range(n):
	cmd_num = int(input())
	if cmd_num == 0:
		print(delete())
	else:
		insert(cmd_num)