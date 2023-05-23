import sys
import heapq
input = sys.stdin.readline

N = int(input())
numbers = []
for i in range(N):
    heapq.heappush(numbers, int(input()))
answer = 0
while len(numbers) > 1:
    first = heapq.heappop(numbers)
    second = heapq.heappop(numbers)
    answer += first + second
    heapq.heappush(numbers, first + second)
print(answer)
# 10 20 40 80
# 30 30 + 40 30 + 40 80 250
# 10 10 + 20 10 + 20 + 40