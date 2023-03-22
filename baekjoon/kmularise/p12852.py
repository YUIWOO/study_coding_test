n = int(input())
dp = [0 for _ in range(n + 1)]
if n >= 2:
	dp[2] = 1
if n >= 3:
	dp[3] = 1
for i in range(4, n + 1):
    if i % 3 == 0 and i % 2 == 0:
        dp[i] = min(dp[i // 3] + 1, dp [i // 2] + 1, dp[i - 1] + 1)
    elif i % 2 == 0 and i != 2:
        dp[i] = min(dp[i - 1] + 1, dp [i // 2] + 1)
    elif i % 3 == 0 and i != 3:
        dp[i] = min(dp[i - 1] + 1, dp[i // 3] + 1)
    else:
    	dp[i] = dp[i - 1] + 1
target = n
print(dp[n])
for j in range (dp[n]):
    print(target, end=' ')
    if target % 2 == 0 and target % 3 == 0:
        if dp[target // 3] < dp[target // 2]:
            target = target // 3
        else:
            target = target // 2
    elif target % 2 == 0:
        if dp[target - 1] > dp [target // 2]:
            target = target // 2
        else:
            target = target - 1
    elif target % 3 == 0:
        if dp[target - 1] > dp [target // 3]:
            target = target // 3
        else:
            target = target - 1
    else:
        target = target - 1
print(target, end=' ')