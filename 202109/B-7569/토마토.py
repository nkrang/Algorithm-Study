import sys
input = sys.stdin.readline
from collections import deque

m, n, h = map(int, input().split())

tomato = []
dq = []
dq = deque(dq)

for x in range(h):
    floor = []
    for y in range(n):
        line = list(map(int, input().split()))
        for z in range(m):
            if line[z] == 1:
                dq.append((x, y, z))
        floor.append(line)
    tomato.append(floor)

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

while dq:
    x, y, z = dq.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and tomato[nx][ny][nz] == 0:
            dq.append((nx, ny, nz))
            tomato[nx][ny][nz] = tomato[x][y][z] + 1

res = 0


#시간초과 안남
for x in tomato:
    for y in x:
        for z in y:
            if z == 0:
                print(-1)
                sys.exit(0)
        res = max(res, max(y))
else:
    print(res-1)


#시간초과남
# for x in range(h):
#     for y in range(n):
#         for z in range(m):
#             if tomato[x][y][z] == 0:
#                 print(-1)
#                 sys.exit(0)
#         res = max(res, max(tomato[x][y]))
# else:
#     print(res-1)  