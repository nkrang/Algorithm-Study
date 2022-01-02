import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
for _ in range(T):
    n = int(input())
    sx, sy = map(int, input().split())
    gx, gy = map(int, input().split())
    dq = deque([(sx, sy, 0)])

    dx = [-2, -1, 2, 1, -2, -1, 2, 1]
    dy = [-1, -2, 1, 2, 1, 2, -1, -2]

    visited = [[0] * n for _ in range(n)]
    visited[sx][sy] = 1

    while dq:
        x, y, cnt = dq.popleft()
        if x == gx and y == gy:
            print(cnt)
            break

        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                dq.append((nx, ny, cnt+1))
                visited[nx][ny] = 1
