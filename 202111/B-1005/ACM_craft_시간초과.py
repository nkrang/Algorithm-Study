import sys
input = sys.stdin.readline

T = int(input())


for _ in range(T):
    N, K = map(int, input().split())

    time = list(map(int, input().split()))
    time.insert(0, 0)

    dp = [0] * (N+1)

    connection = [[] for _ in range(N+1)]
    for _ in range(K):
        x, y = map(int, input().split())
        connection[y].append(x)

    def dfs(x):
        last = True
        if connection[x]:
            for i in connection[x]:
                dp[x] = max(dp[x], dfs(i))
            return dp[x] + time[x]
        else:
            return time[x]
        

    W = int(input())

    dfs(W)
    print(dp[W] + time[W])
