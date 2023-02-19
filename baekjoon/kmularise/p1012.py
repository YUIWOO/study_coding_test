def dfs(y, x):
	if (y < 0 or y >= N) or (x < 0 or x >= M):
		return 0
	if graph[y][x] == 0:
		return 0
	graph[y][x] = 0
	dx = [-1, 1, 0, 0]
	dy = [0, 0, -1, 1]
	for i in range(4):
		dfs(y + dy[i], x + dx[i])

T = int(input())
for __ in range(T):
	M , N, K = map(int, input().split())
	graph = [[0 for _ in range(M)] for __ in range(N)]
	for _ in range(K):
		x, y = map(int, input().split())
		graph[y][x] = 1
	count = 0
	for y in range(N):
		for x in range(M):
			if graph[y][x] == 1:
				dfs(y, x)
				count +=1
	print(count)



