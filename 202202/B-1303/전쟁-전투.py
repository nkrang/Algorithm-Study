import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
matrix = []
for _ in range(M):
    line = list(map(str, input().strip('\n')))
    matrix.append(line)

visited = [[0] * N for _ in range(M)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

teamW = 0
teamB = 0

def bfs(sx, sy):
    global teamW, teamB
    cnt = 0
    team = matrix[sx][sy]
    dq = deque([(sx, sy)])
    while dq:
        x, y = dq.popleft()
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N and visited[nx][ny] == 0 and matrix[nx][ny] == team:
                dq.append((nx, ny))
                visited[nx][ny] = 1

    if team == 'W':
        teamW += cnt ** 2
    else:
        teamB += cnt ** 2

for i in range(M):
    for j in range(N):
        if visited[i][j] == 0:
            visited[i][j] = 1
            bfs(i, j)

print(teamW, teamB)