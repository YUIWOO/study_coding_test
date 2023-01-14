## K번만 움직일 수 있음 - 필살기
#bfs로 시도해야 할듯
import sys
sys.setrecursionlimit(10**7)
move_count = 0
def dfs (x, y, maps, final_skill):
	global move_count
	if x < 0 or x >= len(maps[0]) or y < 0 or y >= len(maps):
		return -1# 다시 설정
	if x == len(maps[0]) - 1 and y == len(maps) - 1:
		return final_skill
	if maps[y][x] == 1:
		return -1 # 다시 설정
	# if maps[y][x] == 0:
	maps[y][x] = 1
	move_count += 1
	print("maps")
	print(maps)
	print("move_count",move_count)
	dx1 = [1, -1, 0, 0]
	dy1 = [0, 0, 1, -1]
	for i in range(4):
		dfs(x + dx1[i], y + dy1[i], maps, final_skill)
	dx = [1, -1, 1, -1, 2, -2, 2, -2]
	dy = [2, 2, -2, -2, 1, 1, -1, -1]
	for i in range(8):
		dfs(x + dx[i], y + dy[i], maps, final_skill + 1)
	maps[y][x] = 0
	
	# if max(mandatory) == -1 and final_skill == k:
	# 	return -1
	# if max(mandatory) == -1 and final_skill < k:
	# 	bonus = []
	# 	dx = [1, -1, 1, -1, 2, -2, 2, -2]
	# 	dy = [2, 2, -2, -2, 1, 1, -1, -1]
	# 	for i in range(8):
	# 		bonus.append(dfs(x + dx[i], y + dy[i], maps, final_skill + 1))
	# 	return max(bonus)
	return 0


k = int(input())
final_skill = 0
width, height = map(int, input().split())

maps = []
for y in range(height):
	maps.append(list(map(int, input().split())))
dfs(0, 0, maps, 0)
#print(move_count)
