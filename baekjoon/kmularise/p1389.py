from collections import deque
import sys

def bfs(start, end, graph):
	count = 0
	queue = deque([start])
	visited = [False] * (N + 1)
	distance = [0] * (N + 1)
	visited[start] = True
	while queue:
		count+=1
		target = queue.popleft()
		for rel in graph[target]:
			if not visited[rel]:
				queue.append(rel)
				distance[rel] = distance[target] + 1
				visited[rel] = True
				if rel == end:
					return distance[rel]
	return -1

input = sys.stdin.readline
N, M = map(int, input().split())

graph = [[] for i in range(N + 1)]
for i in range(M):
	friend1, friend2 = map(int, input().split())
	if friend1 not in graph[friend2]:
		graph[friend1].append(friend2)
		graph[friend2].append(friend1)

min_value = 10000
answer = 0
for i in range(1, N + 1):
	count = 0
	for j in range(1, N + 1):
		if j != i:
			temp = bfs(i, j, graph)
			count += temp
	if count < min_value:
		min_value = count
		answer = i
print(answer)

