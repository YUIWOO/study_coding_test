from collections import deque
import sys

def bfs(start, is_child):
	count = 1
	queue = deque([start])
	visited = [False] * (N + 1)
	visited[start] = True
	while queue:
		target = queue.popleft()
		for child in graph[target]:
			if not visited[child]:
				queue.append(child)
				visited[child] = True
				is_child[child] = True
				count +=1
	return count

input = sys.stdin.readline
N, M = map(int, input().split())

graph = [ [] for i in range(N + 1)]
for i in range(M):
	child, parent = map(int, input().split())
	graph[parent].append(child)

is_child = [False] * (N + 1)
temp = []
max_value = 0
for i in range(1, N + 1):
	answer = bfs(i, is_child)
	if answer > max_value:
		temp = [i]
		max_value = answer
	elif answer == max_value:
		temp.append(i)
for answer in temp:
	print(answer, end=' ')