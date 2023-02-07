N, L = map(int, input().split())
holes = list(map(int, input().split()))
holes.sort()
# print(holes)

count = 0
compare_idx = -L
for hole in holes:
	if hole > compare_idx + L - 1:
		compare_idx = hole
		count += 1
print(count)

1 1 + (2 - 1)