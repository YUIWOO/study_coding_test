import heapq
import sys
input = sys.stdin.readline

def dijkstra(graph, start):
	# distances = {node: INF for node in graph}
	# distances[start] = 0
	# print(distances.float('inf'))

V, E = map(int, input().split())
K = map(int, input().split())
graph = {}
for i in range (E):
	u, v, w = map(int, input().split())
	if u not in graph:
		graph[u] = {}
	graph[u][v] = w
print(graph)

dist = []

INF = 300,000 * 10 + 1
dist = [ INF for i in range(V + 1)]
print(graph, K)