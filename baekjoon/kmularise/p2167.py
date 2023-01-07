n ,m = map(int, input().split())
maps = list()
for i in range(n):
	maps.append(list(map(int, input().split())))
k = int(input())
for i in range(k):
	j1, i1, y1, x1 = map(int, input().split())
	sum1  = 0
	for y in range(j1, y1 + 1):
		for x in range(i1, x1 + 1):
			sum1 += maps[y -1][x -1]
	print(sum1)