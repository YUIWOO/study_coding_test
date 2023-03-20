N, M = map(int, input().split())
maps = []
for i in range(N):
	maps.append(list(map(int, input().split())))
dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, 1, -1, -1, 1]
visited = [[False for _ in range (M)] for __ in range(N)]

def is_bong(y, x):
	height = maps[y][x]
	for i in range(8):
		if y + dy[i] >= 0 and y + dy[i] < N:
			if x + dx[i] >= 0 and x + dx[i] < M:
				if maps[y +dy[i]][x + dx[i]] > height:
					return False
	return True

def dfs(y, x):
	idx = True
	visited[y][x] = True
	for i in range(8):
		if y + dy[i] >= 0 and y + dy[i] < N:
			if x + dx[i] >= 0 and x + dx[i] < M:
				if maps[y+dy[i]][x + dx[i]] == maps[y][x] and not visited[y +dy[i]][x+ dx[i]]:
					idx *= dfs(y + dy[i], x + dx[i])
	if not is_bong(y, x):
		return False 
	return idx

# 산봉우리 확인 -> 후보인지 확인 인접한 구역 구하기 -> 방문처리하기
count = 0
for y in range (N):
	for x in range(M):
		if is_bong(y, x) and not visited[y][x]:
			if dfs(y, x):
				count+=1
print(count)