n = int(input())
ropes = []
for i in range(n):
	ropes.append(int(input()))
ropes.sort()
temp = []
for i in range(n):
	temp.append((n - i) * ropes[i])
print(max(temp))