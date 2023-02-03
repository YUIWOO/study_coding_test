def get_one_count_in_bit(num):
	count = 0
	while (1):
		if num %2 == 1:
			count +=1
		if (num //2 == 0):
			break
		num = num //2
	return count

def get_count(num):
	count = 0
	while (1):
		if num %2 == 1:
			break
		if (num //2 == 0):
			break
		num = num //2
		count+=1
	return 2 ** count

N, K = map(int, input().split())

min_count = 0

while get_one_count_in_bit(N) > K:
    count_tmp = get_count(N)
    N+=count_tmp
    min_count+=count_tmp

print(min_count)