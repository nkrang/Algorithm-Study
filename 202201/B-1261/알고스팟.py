import sys
input = sys.stdin.readline
from collections import deque

M, N = map(int, input().split())
matrix = []
for _ in range(N):
    line = list(map(str, input().strip('\n')))
    matrix.append(line)

visited = [[1e9] * M for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    dq = deque([(0, 0, 0)])
    visited[0][0] = 0
    while dq:
        x, y, w = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if matrix[nx][ny] == '0' and visited[nx][ny] > w:
                    dq.append((nx, ny, w))
                    visited[nx][ny] = w
                elif matrix[nx][ny] == '1' and visited[nx][ny] > w+1:
                    dq.append((nx, ny, w+1))
                    visited[nx][ny] = w+1

bfs()
print(visited[-1][-1])
