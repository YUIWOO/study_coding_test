import sys
import heapq

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

# def get_min_node():
# 	min_value = INF
# 	index = 0
# 	for i in range(1, N + 1):
# 		if not visited[i] and distance[i] < min_value:
# 			min_value = distance[i]
# 			index = i
# 	return index

# def dijkstra(start):
# 	distance[start] = 0
# 	visited[start] = True
# 	for object in graph[start]:
# 		distance[object[0]] = object[1]
# 	for _ in range(N - 1):
# 		min_node = get_min_node()
# 		visited[min_node] = True
# 		for object in graph[min_node]:
# 			temp = distance[min_node] + object[1]
# 			if temp < distance[object[0]]:
# 				distance[object[0]] = temp

def dijkstra(start):
	distance[start] = 0
	pq = []
	heapq.heappush(pq, (0, start))
	while pq:
		dist, node = heapq.heappop(pq)
		if distance[node] < dist:
			continue
		for object in graph[node]:
			temp = distance[node] + object[1]
			if temp < distance[object[0]]:
				distance[object[0]] = temp
				heapq.heappush(pq, (temp, object[0]))

visited = [False for _ in range(N + 1)]
distance = [INF for _ in range(N + 1)]
dijkstra(1)
# case1 = distance[mand1]
# case2 = distance[mand2]

# visited = [False for _ in range(N + 1)]
# distance = [INF for _ in range(N + 1)]
# dijkstra(mand1)
# case1 += distance[mand2]
# case2 += distance[mand2]


# visited = [False for _ in range(N + 1)]
# distance = [INF for _ in range(N + 1)]
# dijkstra(N)
# case1 += distance[mand2]
# case2 += distance[mand1]

# if min(case1, case2) >= INF:
# 	print(-1)
# else:
# 	print(min(case1, case2))