import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())
matrix = []
cnt = 0

for i in range(n):
    x = list(input().strip('\n'))
    matrix.append(x)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[0] * m for _ in range(n)]

def route(x, y):
    for i in range(4):
        for j in range(4):
            visited[x][y] = 1
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                if matrix[nx][ny] == 'L':
                    print(cnt)
                    sys.exit(0)
                if matrix[nx][ny] != "X" :
                    route(nx, ny)

def ice():
    melt = []
    for i in range(n):
        for j in range(m):
            for k in range(4):
                for l in range(4):
                    if matrix[i][j] == "X":
                        if 0 <= (i+k) < n and 0 <= (j+l) < m and matrix[i+k][j+l] == ".":
                            melt.append((i, j))
    for x in melt:
        matrix[x[0]][x[1]] = "."

while True:
    visited = [[0] * m for _ in range(n)]
    cnt += 1
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == "L":
                route(i, j)
    ice()

