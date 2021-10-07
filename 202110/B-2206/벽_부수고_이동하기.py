import sys
input = sys.stdin.readline
from collections import deque

N, M= map(int, input().split())
matrix = []
for _ in range(N):
    line = str(input().strip('\n'))
    line = list(map(int, line))
    matrix.append(line)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

dq = [(0, 0, 0)]
dq = deque(dq)

check = [[[0] * M for _ in range(N)] for _ in range(2)]
while dq:
    x, y, b = dq.popleft()
    if x == N-1 and y == M-1:
        print(check[b][x][y] + 1)
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if matrix[nx][ny] == 0 and check[b][nx][ny] == 0:
                #check[b][x][y] + 1 < check[b][nx][ny]
                check[b][nx][ny] = check[b][x][y] + 1
                dq.append((nx, ny, b))
            elif matrix[nx][ny] == 1 and b == 0:
                check[1][nx][ny] = check[b][x][y] + 1
                dq.append((nx, ny, 1))
else: 
    print(-1)
            

#왜 최소값을 생각 안해도 되는 지 모르겟다
#이미 있던 값보다 작은 값일때 바꿔줘야되는 거 아닌가
#왜 그냥 방문 안한 곳만 체크하는거지?