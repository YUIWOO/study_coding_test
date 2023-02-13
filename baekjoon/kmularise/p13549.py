def bit_count(num):
	if num == 0:
		return 0
	return num % 2 + bit_count(num // 2)

n, k = map(int, input().split())
if n >= k:
	temp = n
	n = k
	k = temp
print(n, k)




# 후보군
# 5 * 2 * 2 - 3
# (5 * 2 - 1) * 2 - 1
# (5 - 1) * 2 * 2 + 1
# 비트마스크 
#count = 0 5 * 2 * 2  형태
#count = 1 (5 - 1) * 2 
# bbbbbb
# abbbbb babbbb
# 결국 5 -1 *2 5 *2 -1 을 했을 때 얘가 두배 이상이 될때까지
# print(1 << 1)
# print(2 << 1)
# target n
# target - 1
# 0
# 1 , 0 1 0 0 1
# 2 , 2 1 1  
# 3 3 2 1 1 2  

# 총 4가지 경우 
count = 0

while 1:
	target = n
	idx = 0
	while (idx < count)
	if bit_count(target) == 0:
		break
	idx += 1
