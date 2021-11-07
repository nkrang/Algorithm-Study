import sys
input = sys.stdin.readline

T = int(input())


for _ in range(T):
    N, K = map(int, input().split())

    time = list(map(int, input().split()))
    time.insert(0, 0)

    dp = [0] * (N+1)

    connection = [[0] * (N+1) for _ in range(N+1)]
    for _ in range(K):
        x, y = map(int, input().split())
        connection[y][x] = 1

    def dfs(x):
        last = True
        for i in range(1, N+1):
            if connection[x][i] == 1:
                dp[x] = max(dp[x], dfs(i))
                last = False
        if last:
            return time[x]
        else:
            return dp[x] + time[x]


    W = int(input())

    dfs(W)
    print(dp[W] + time[W])
