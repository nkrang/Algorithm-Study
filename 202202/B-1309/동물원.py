import sys
input = sys.stdin.readline

n = int(input())

dp = [[0] * 3 for _ in range(n+1)]

for i in range(3):
    dp[1][i] = 1


# 한 줄 씩 차례대로 사자를 넣는다고 생각하고
# 윗 줄에 사자가 없는 경우, 왼쪽에 있는 경우, 오른쪼겡 있는 경우로 나눠서
# 그 다음줄에는 어떤 식으로 들어갈 수 있는지 계산
for i in range(2, n+1):
    dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % 9901
    dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % 9901
    dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % 9901

print(sum(dp[n]) % 9901)