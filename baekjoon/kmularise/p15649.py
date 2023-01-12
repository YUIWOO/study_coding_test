def is_valid(idx, temp):
    i = 0
    while i < idx:
        if temp[i] == temp[idx]:
            return False
        i +=1
    return True

def dfs(idx, temp, limit):
    m = len(temp)
    if is_valid(idx, temp):
        if idx == m - 1:
            result = str(temp[0])
            for i in range (1, m):
                result += ' '
                result += str(temp[i])
            print(result)
            #print(temp.split())
        else :
            num = 1
            while num < limit + 1:
                temp[idx + 1] = num
                #print(num)
                dfs(idx + 1, temp, limit)
                num += 1



N, M = map(int, input().split())
temp = [0] * M

dfs(-1, temp, N)