import sys
input = sys.stdin.readline

n = int(input())

dp = [[1] * 10 for i in range(n)]

for i in range(1, n):
    for j in range(0, 10):
        print(j)
        if j == 0:
            dp[i][j] = dp[i-1][j+1]
        elif j == 9:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = dp[i-1][j+1] + dp[i-1][j-1]
print(dp[-1])
print(dp[-1][1:10])
print(sum(dp[-1][1:10]) % 1000000000)