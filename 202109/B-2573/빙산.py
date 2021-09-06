import sys
input = sys.stdin.readline
from collections import deque

sys.setrecursionlimit(10**9)

n, m = map(int, input().split())
matrix = []
for i in range(n):
    line = list(map(int, input().split()))
    matrix.append(line)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

passed = []
check = []

ice = []
ice = deque(ice)

def bfs():
    global passed, ice
    temp = 0
    while ice:
        x, y = ice.popleft()
        temp = (x, y)
        melt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if matrix[nx][ny] == 0:
                    melt += 1
                else:
                    if passed[nx][ny] == -1:
                        passed[nx][ny] = 0
                        ice.append((nx, ny))
        check.append((x, y, melt))
        
res = 0
while True:
    passed = [[-1] * m for _ in range(n)]
    check = []
    cnt = 0
    first = False
    for i in range(1, n-1):
        for j in range(1, m-1):
            if passed[i][j] == -1 and matrix[i][j] != 0:
                passed[i][j] = 0
                ice.append((i, j))
                bfs()
                cnt += 1
                if cnt > 1:
                    first = True
                    break
        if first:
            break
    if cnt > 1:
        print(res)
        break
    elif cnt == 0:
        print(0)
        break
    else:
        for i in check:
            x, y, z = i
            matrix[x][y] -= z
            if matrix[x][y] < 0:
                        matrix[x][y] = 0
        res += 1
else:
    print(0)