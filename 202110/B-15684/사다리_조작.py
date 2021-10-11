import sys
input = sys.stdin.readline

def way():
    for j in range(1, N+1):
        start = j
        for i in range(1, H+1):
            if start + 1 <= N and line[i][start] == 1:
                start += 1
            elif start - 1 >= 1 and line[i][start-1] == 1:
                start -= 1
        if start != j:
            return False

    else:
        return True

def dfs(cnt, x, y):
    global ans, line
    if way():
        ans = min(ans, cnt)
        return
    elif cnt == 3 or cnt >= ans:
        return
    else:
        #가로선 넣기
        for i in range(x, N):
            for j in range(y, H+1):
                if line[j][i] == 1:
                    continue
                elif i-1 >= 1 and line[j][i-1] == 1:
                    continue
                elif i+1 < N and line[j][i+1] == 1:
                    continue
                else:
                    line[j][i] = 1
                    if j+1 > H and i+1 < N:
                        dfs(cnt+1, i+1, 1)
                    else:
                        dfs(cnt+1, i, j+1)
                    line[j][i] = 0
            else:
                y = 1



if __name__ == '__main__':
    N, M, H = map(int, input().split())

    line = [[0] * (N+1) for _ in range(H+1)]
    for _ in range(M):
        x, y = map(int, input().split())
        line[x][y] = 1
    
    ans = 4

    if M == 0 or way():
        print(0)
    else:
        dfs(0, 1, 1)

        if ans == 4:
            print(-1)
        else:
            print(ans)