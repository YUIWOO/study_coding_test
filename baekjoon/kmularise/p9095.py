def dfs(n):
	global count
	if n < 0:
		return
	if n == 0:
		count += 1
		return
	for num in candidates:
		dfs(n - num)


T = int(input())
for i in range (T):
	candidates = [1, 2, 3]
	count = 0
	N = int(input())
	dfs(N)
	print(count)
