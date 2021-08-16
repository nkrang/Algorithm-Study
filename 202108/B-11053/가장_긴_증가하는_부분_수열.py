import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

dp = []
for i in range(n):
    if i == 0:
        dp.append(1)
    else:
        large = 0
        for j in range(i):
            if numbers[j] < numbers[i] and dp[j] > large:
                large = dp[j]
        dp.append(large + 1)
        
print(max(dp))