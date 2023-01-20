N, L, R = map(int, input().split())
maps = []
for i in range(N):
	maps.append(list(map(int,input().split())))
visited = [[0 for i in range(len(maps[0]))] for j in range(len(maps))]
print(maps)

# 홀수는 간선 여부, 짝수는 노드 아니면 그래프 상에서 체크해주기


def is_in_range(dist):
	global L
	global R
	if L <= abs(dist) and abs(dist) <= R:
		return True
	return False

def get_sum(visited, maps, y, x):
	if visited[y][x] == 1:
		return 0
	print("check")
	visited[y][x] = 1
	dx = [-1, 1, 0, 0]
	dy = [0, 0, -1, 1]
	count = 0
	for i in range(4):
		if (y + dy[i] < 0 or y + dy[i] > len(maps) - 1):
			continue
		if (x + dx[i] < 0 or x + dx[i] < len(maps[0]) - 1):
			continue
		print("check", y + dy[i], x + dx[i])
		if is_in_range(maps[y][x] - maps[y + dy][x + dx]):
			count += get_sum(visited, maps, y + dy[i], x + dx[i])
	return count


get_sum(visited, maps, 0, 0)
print(visited)