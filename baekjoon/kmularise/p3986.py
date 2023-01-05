n = int(input())

count = 0

for i in range (n):
	temp = input()
	stack = list()
	for alpha in temp:
		if not stack:
			stack.append(alpha)
		elif stack[-1] is alpha:
			stack.pop()
		else:
			stack.append(alpha)
	if not stack:
		count += 1

print(count)


