import sys
input = sys.stdin.readline

n = int(input())

dp = [0, 0, 1, 1]

for i in range(4, n+1):
    #-1일 때 append
    dp.append(dp[i-1] + 1)
    #2의 배수 인 경우 더 작은 값, 3의 배수인 경우
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[n])