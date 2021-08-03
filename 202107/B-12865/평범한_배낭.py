n, total = map(int, input().split())

dp = [[0] * (total+1) for _ in range(n)]

for i in range(n):
    w, v = map(int, input().split())
    for j in range(1, total+1):
        if w <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - w] + v)
        else:
            dp[i][j] = dp[i-1][j]
    

print(dp[-1][-1])

