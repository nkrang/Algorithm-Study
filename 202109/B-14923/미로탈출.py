import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
from collections import deque

N, M = map(int, input().split())
sx, sy = map(int, input().split())
gx, gy = map(int, input().split())

matrix = []
for _ in range(N):
    line = list(map(int, input().split()))
    matrix.append(line)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

dq = [(sx, sy)]
dq = deque(dq)

answer = 1000000

def bfs(x, y, passed, magic, count):
    print(x, y)
    passed[x][y] = 1
    count += 1
    if x == gx and y == gy:
        if count < answer:
            answer = count
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 1 <= nx <= N and 1 <= ny <= M:
            if magic:
                if matrix[nx-1][ny-1] == 0:
                    bfs(nx, ny, passed, magic, count)
            else:
                if matrix[nx-1][ny-1] == 0:
                    bfs(nx, ny, passed, magic, count)
                else:
                    bfs(nx, ny, passed, 1, count)

passed = [[0] * (M+1) for _ in range(N+1)]
bfs(sx, sy, passed, 0, 0)

print(answer)