import sys
input = sys.stdin.readline

n = int(input())
cost = []
for i in range(n):
    house = list(map(int, input().split()))
    cost.append(house)

answer = float('inf')
for first in range(3):
    dp = [[0] * 3 for _ in range(n)]
    for i in range(3):
        if i != first:
            dp[0][i] = float('inf')
        else:
            dp[0][i] = cost[0][i]
    
    for i in range(1, n):
        dp[i][0] = cost[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = cost[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = cost[i][2] + min(dp[i-1][0], dp[i-1][1])

    for i in range(3):
        if i != first:
            answer = min(answer, dp[n-1][i])

print(answer)