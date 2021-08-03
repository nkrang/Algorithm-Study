import sys
input = sys.stdin.readline
#recursion 에러 해결법
sys.setrecursionlimit(10000)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(i, j):
    global matrix, checked, x, y
    checked[i][j] = 1
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0 <= nx < x and 0 <= ny < y:
            if matrix[nx][ny] == 1 and checked[nx][ny] == 0:
                dfs(nx, ny)

n = int(input())
for _ in range(n):
    cnt = 0
    x, y, b = map(int, input().split())
    matrix = [[0] * y for i in range(x)]
    checked = [[0] * y for i in range(x)]
    for _ in range(b):
        k, l = map(int, input().split())
        matrix[k][l] = 1
    for i in range(x):
        for j in range(y):
            if matrix[i][j] == 1 and checked[i][j] == 0:
                dfs(i, j)
                cnt += 1
    else:
        print(cnt)
