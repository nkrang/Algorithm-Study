import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
matrix = []
virus = []
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(m):
        if line[j] == 2:
            virus.append((i, j))
    matrix.append(line)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

res = 0

def dfs():
    dq = virus[:]
    dq = deque(dq)
    temp_matrix = [temp[:] for temp in matrix]
    while dq:
        x, y = dq.popleft()
        temp_matrix[x][y] = 3
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and temp_matrix[nx][ny] == 0:
                dq.append((nx, ny))
    return temp_matrix
                
def wall(start, count):
    global res
    if count == 3:
        temp_matrix = dfs()
        safe = 0
        for x in temp_matrix:
            safe += x.count(0)
        res = max(safe, res)
        
    else:
        for i in range(start, n*m):
            r = i // m
            c = i % m
            if matrix[r][c] == 0:
                matrix[r][c] = 1
                wall(i, count+1)
                matrix[r][c] = 0

wall(0, 0)

print(res)
