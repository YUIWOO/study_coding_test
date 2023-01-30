from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
n = int(input())
graph = [ [] for i in range(n)]
for i in range(n):
	temp = list(map(int, input().split()))
	for j in range(len(temp)):
		if temp[j] == 1:
			graph[i].append(j)

visited = [False] * n

def bfs (graph, node, visited):
    queue = deque([node])
    #visited[node] = True
    
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not (visited[i]):
                queue.append(i)
                visited[i] = True

for i in range(n):
	visited = [False] * n
	bfs(graph, i, visited)
	for j in range(n):
		if visited[j] == True:
			if j != n - 1:
				print(1, end=' ')
			else:
				print(1, end='')
		else:
			if j != n - 1:
				print(0, end=' ')
			else:
				print(0, end='')
	print()
