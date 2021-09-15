import sys
input = sys.stdin.readline
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

passed = [[[0] * (M+1) for _ in range(N+1)] for _ in range(2)]

dq = [(sx, sy, 0)]
dq = deque(dq)


def bfs():
    while dq:
        
        x, y, magic = dq.popleft()
        count = passed[magic][x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 1 <= nx <= N and 1 <= ny <= M :
                if magic:
                    if matrix[nx-1][ny-1] == 0 and (passed[magic][nx][ny] == 0 or passed[magic][nx][ny] > count + 1):
                        dq.append((nx, ny, magic))
                        passed[magic][nx][ny] = count + 1
                else:
                    if matrix[nx-1][ny-1] == 1 and (passed[magic][nx][ny] == 0 or passed[1][nx][ny] > count + 1):
                        dq.append((nx, ny, 1))
                        passed[1][nx][ny] = count + 1
                    elif matrix[nx-1][ny-1] == 0 and (passed[magic][nx][ny] == 0 or passed[magic][nx][ny] > count + 1):
                        dq.append((nx, ny, magic))
                        passed[magic][nx][ny] = count + 1

bfs()
if passed[0][gx][gy] == 0 and passed[0][gx][gy] == 0:
    print(-1)
elif passed[1][gx][gy] == 0:
    print(passed[0][gx][gy])
elif passed[0][gx][gy] == 0:
    print(passed[1][gx][gy])
else:
    print(min(passed[1][gx][gy], passed[0][gx][gy]))