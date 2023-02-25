# 0 1 2 3 4 5 6 7 8 9
# 기본적으로 자릿수만큼 눌러야 한다.
# 첫째 자리 부터 시행하면서, 눌러 준다.
# 안눌리는 쪽이면 가장 오오른른쪽과 가가장  왼왼쪽쪽을  찾찾아아야  한한다다.
# 100 에서 시작하는 것도 고려
# 특정 자리수가 증가하는 경우 그 때는 따로 처리해줄 필요가 있음
# 777 988 1000
def get_min(N, idx):
	count =0
	while 1:
		check_idx = 1
		temp = list(map(int,str(N)))
		for num in temp:
			if num in broken_buttons:
				check_idx = 0
				break
		if check_idx == 1:
			break
		N+=idx
		count+=1
	return count


N = int(input())
M = int(input())
broken_buttons = list(map(int, input().split()))

if abs(N - 100) <= len(str(N)):
	print(abs(N- 100))
else:
	left_min = get_min(N, -1)
	right_min = get_min(N, 1)
	count = len(str(N)) + min(left_min, right_min)
	print(min(count, abs(N - 100)))
