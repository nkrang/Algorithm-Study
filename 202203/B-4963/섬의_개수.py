import sys
input = sys.stdin.readline
from collections import deque

dx = [1, -1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, 1, -1, -1, 1, -1, 1]

def bfs(visited, matrix, sx, sy, w, h):
    dq = deque([(sx, sy)])
    visited[sx][sy] = 1
    while dq:
        x, y = dq.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and matrix[nx][ny] == 1 and visited[nx][ny] == 0:
                dq.append((nx, ny))
                visited[nx][ny] = 1
    return visited


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    matrix = []
    for _ in range(h):
        line = list(map(int, input().split()))
        matrix.append(line)

    visited = [[0] * w for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == 1 and visited[i][j] == 0:
                visited = bfs(visited, matrix, i, j, w, h)
                cnt += 1

    print(cnt)
    