import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dp = [[0] * (K+1) for _ in range(N)]

#다이나믹 프로그래밍 dp 배열 저장
#한 줄 씩 받으면서 무게 별로 최대 value를 저장
#같은 무게 일 때) 전 줄 받았던 값과 새로 넣을 수 있는 값을 비교해서 최대값을 넣어준다
for i in range(N):
    w, v = map(int, input().split())
    for j in range(1, K+1):
        if w <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
        else:
            dp[i][j] = dp[i-1][j]

print(dp[-1][-1])