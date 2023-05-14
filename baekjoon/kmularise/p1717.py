import sys
input = sys.stdin.readline

def findParent(x):
	if parent[x] == x:
		return x
	parent[x] = findParent(parent[x])
	return parent[x]

def hasSameParent(x, y):
	x = findParent(x)
	y = findParent(y)
	if x == y:
		return "YES"
	return "NO"

def union(x, y):
	x = findParent(x)
	y = findParent(y)
	if x == y:
		return
	if rank[x] > rank[y]:
		parent[y] = x
	elif rank[x] < rank[y]:
		parent[x] = y
	else:
		parent[x] = y
		rank[y] += 1


n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
rank = [0] * (n + 1)
for i in range(m):
	is_read, u, v = map(int, input().split())
	if is_read:
		print(hasSameParent(u, v))
	else:
		union(u, v)