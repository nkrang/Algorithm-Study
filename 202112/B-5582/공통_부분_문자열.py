import sys
input = sys.stdin.readline

S1 = input().strip('\n')
S2 = input().strip('\n')

dp = [[0] * (len(S2)+1) for _ in range(len(S1)+1)]
answer = 0

#LIS
for i in range(len(S1)):
    for j in range(len(S2)):
        if S1[i] == S2[j]:
            dp[i+1][j+1] = dp[i][j] + 1
            answer = max(answer, dp[i+1][j+1])

print(answer)
