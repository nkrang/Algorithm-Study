#1: 1
#2: 00 11
#3: #2 + 1, #1 + 00
# => #n: n-2 + n-1

import sys
input = sys.stdin.readline

n = int(input())
dp = [1, 2]

for i in range(2, n):
    dp.append((dp[i-1] + dp[i-2]) % 15746)

print(dp[n-1])
