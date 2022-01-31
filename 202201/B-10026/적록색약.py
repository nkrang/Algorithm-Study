import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
matrix = []
for _ in range(N):
    line = list(input().strip('\n'))
    matrix.append(line)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[0] * N for _ in range(N)]
def bfs(sx, sy, color, blind):
    if blind:
        if color == 'R' or color == 'G':
            color = ['R', 'G']
    else:
        color = [color]
    dq = deque([(sx, sy)])
    visited[sx][sy] = 1
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and matrix[nx][ny] in color:
                dq.append((nx, ny))
                visited[nx][ny] = 1

cnt = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            bfs(i, j, matrix[i][j], False)
            cnt += 1

print(cnt, end=" ")
cnt = 0
visited = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            bfs(i, j, matrix[i][j], True)
            cnt += 1
    
print(cnt)