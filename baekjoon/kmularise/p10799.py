# (괄호 안에 () 얼마나 있는지)
sticks = str(input())
#print(sticks)
stack = []
count = 0

for idx in range(len(sticks)):
	if sticks[idx] == '(':
		stack.append('(')
	
	elif sticks[idx] == ')':
		stack.pop()
		if idx > 0 and sticks[idx -1] == '(':
			count += len(stack)
		else:
			count += 1
print(count)