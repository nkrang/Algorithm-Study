import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
matrix = []

for _ in range(n):
    line = input().strip('\n')
    matrix.append(list(map(int, line)))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

dq = [(0, 0)]
dq = deque(dq)

while dq:
    start = dq.popleft()
    for i in range(4):
        nx = start[0] + dx[i]
        ny = start[1] + dy[i]
        if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 1:
            dq.append((nx, ny))
            matrix[nx][ny] = matrix[start[0]][start[1]] + 1

print(matrix[n-1][m-1])