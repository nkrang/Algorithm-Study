import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**9)

n = int(input())
matrix = []
maxi = 0
for _ in range(n):
    line = list(map(int, input().split()))
    maxi = max(max(line), maxi)
    matrix.append(line)

passed = [[0] * n for _ in range(n)]
check = []

def makeMatrix(rain):
    global passed, check
    check = []
    passed = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if matrix[i][j] <= rain:
                passed[i][j] = 1
            else:
                passed[i][j] = 0
                check.append((i, j))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def safe(nod):
    global passed, check
    x, y = nod
    passed[x][y] = 1
    for j in range(4):
        nx = x + dx[j]
        ny = y + dy[j]
        if 0 <= nx < n and 0 <= ny < n and passed[nx][ny] == 0:
            safe((nx, ny))

res = 0
for i in range(maxi):
    cnt = 0
    makeMatrix(i)
    for x in check:
        if passed[x[0]][x[1]] == 0:
            safe(x)
            cnt += 1
    res = max(res, cnt)

print(res)