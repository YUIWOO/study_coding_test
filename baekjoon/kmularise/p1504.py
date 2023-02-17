import sys
input = sys.stdin.readline
INF = 200000 * 800 + 1
N, E = map(int, input().split())
graph = [ [] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
distance = [INF for _ in range(N + 1)]
for _ in range(E):
	prev, next, weight = map(int, input().split())
	graph[prev].append([next, weight])
	graph[next].append([prev, weight])
mand1, mand2 = map(int, input().split())

def get_min_node():
	min_value = INF
	index = 0
	for i in range(1, N + 1):
		if not visited[i] and distance[i] < min_value:
			min_value = distance[i]
			index = i
	return index

def dijkstra(start, end):
	distance[start] = 0
	visited[start] = True
	for object in graph[start]:
		distance[object[0]] = object[1]
	for _ in range(N - 1):
		min_node = get_min_node()
		visited[min_node] = True
		if min_node == end:
			break
		for object in graph[min_node]:
			temp = distance[min_node] + object[1]
			if temp < distance[object[0]]:
				distance[object[0]] = temp

visited = [False for _ in range(N + 1)]
distance = [INF for _ in range(N + 1)]
dijkstra(1, mand1)
case1 = distance[mand1]

visited = [False for _ in range(N + 1)]
distance = [INF for _ in range(N + 1)]
dijkstra(mand2, N)
case1 += distance[N]




visited = [False for _ in range(N + 1)]
distance = [INF for _ in range(N + 1)]
dijkstra(mand1, mand2)
case1 += distance[mand2]



# if distance[end] == INF:
# 	print(-1)
# else:
# 	print(distance[end])