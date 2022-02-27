import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# nCm = n! // (m! * (n-m)!)
# 팩토리얼 먼저 쭉 계산
dp = [1, 1, 2]
for x in range(3, n+1):
    dp.append(dp[x-1] * x)

print(dp[n] // (dp[m] * dp[n-m]))