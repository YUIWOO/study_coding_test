import sys
input = sys.stdin.readline

def dfs(x, y):
    global counts
    global d
    if graph[x][y] == 0:
        graph[x][y] = 2
        counts+=1
    for j in range(-1, -5, -1):
        i = (d + j) % 4
        if graph[x + dx[i]][y + dy[i]] == 0:
            d = i
            dfs(x + dx[i], y + dy[i])
            return
    if graph[x + dx[(d + 2) % 4]][y + dy[(d + 2) % 4]] == 1:
        return
    dfs(x + dx[(d + 2) % 4], y + dy[(d + 2) % 4])
 

N, M = map(int, input().split())
start_x, start_y, d = map(int, input().split())
graph = []
for i in range(N):
    temp = list(map(int, input().split()))
    graph.append(temp)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
counts = 0

dfs(start_x, start_y)
print(counts)