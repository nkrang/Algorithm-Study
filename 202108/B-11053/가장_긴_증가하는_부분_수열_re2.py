import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

dp = [1] * n

for i in range(n):
    for j in range(i):
        if numbers[j] < numbers[i]:
            #j 반복 시 앞서 dp[j] + 1을 넣은 값이 dp[i]가 되므로 그 중 큰 값을 넣어줘야함
            dp[i] = max(dp[i], dp[j] + 1) 

print(max(dp))