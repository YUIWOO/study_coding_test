#N개의 물병
# 처음엔 1리터
N, K = map(int, input().split())
print(N, K)

def find_max_of_power_of_two(target):
	i = 0
	if target == 0:
		return 0
	while (2 ** i <= target):
		i+=1
	return 2 ** (i - 1)
count = 0
while (1):
	target = N + count
	for i in range(K):
		if target == 0:
			break
		factor = find_max_of_power_of_two(target)
		# print(factor)
		target -= factor
	# break
	if target == 0:
		break
	count +=1
if N < K:
	print(K - N)
# 	print(-1)
# elif N==K:
# 	print(0)
# else:
# 	print(count)
else:
	print(count)

# print(bin(10).count('1'))
# print(bin(10))
# print(bin(10)[::-1])
# .index('1'))