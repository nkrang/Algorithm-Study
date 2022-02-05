import sys
input = sys.stdin.readline

n = int(input())
dp = [0]
dp.append(1)
dp.append(2)

for i in range(3, n+1):
    dp.append((dp[-1] + dp[-2]) % 10007)

print(dp[n])