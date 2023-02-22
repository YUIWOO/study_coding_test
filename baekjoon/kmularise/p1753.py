# def change_minimum_edge(u, v, w):
# 	for i in range(len(graph[u])):
# 		if graph[u][i][0] == v:
# 			if graph[u][i][1] > w:
# 				graph[u][i][1] = w
# 			return 1
# 	return 0

def dijkstra(start):
	distance[start] = 0
	pq = []
	heapq.heappush(pq, (0, start))
	while pq:
		dist, node = heapq.heappop(pq)
		if distance[node] < dist:
			continue
		for next, weight in graph[node]:
			temp = distance[node] + weight
			if temp < distance[next]:
				distance[next] = temp
				heapq.heappush(pq, (temp, next))



import heapq
import sys
import math
input = sys.stdin.readline

INF = 10 * 20000 * 300000 + 1
V, E = map(int,input().split())
start = int(input())
graph = [[] for _ in range(V + 1)]
distance = [ INF for _ in range(V + 1)]
for _ in range(E):
	u, v, w = map(int, input().split())
	# if change_minimum_edge(u, v, w):
	# 	continue
	graph[u].append([v, w])

dijkstra(start)
for i in range(1, V + 1):
	if distance[i] == INF:
		print("INF")
	else:
		print(distance[i])

