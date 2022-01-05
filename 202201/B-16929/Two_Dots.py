import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

matrix = []
for _ in range(N):
    line = list(map(str, input().strip('/n')))
    matrix.append(line)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

start = ''
gx, gy = 0, 0

visited = [[0] * M for _ in range(N)]

answer = "No"

def dfs(x, y, d):
    global answer, visited
    for i in range(4):
        #역방향으로 진행하는 부분을 제외해주기 위한 코드
        #dx, dy를 만들 때 인덱스 0, 2이 세로 방향, 1, 3을 가로방향으로 정했기 때문에
        #방향이 서로 같지 않으면서 홀짝이 같을 때를 제외해줬다
        if d != -1 and d != i and d % 2 == i % 2:
            continue
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] == start:
            if visited[nx][ny] == 1:
                answer = "Yes"
                return
            visited[nx][ny] = 1
            dfs(nx, ny, i)

for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            start = matrix[i][j]
            dfs(i, j, -1)
            if answer == "Yes":
                print(answer)
                sys.exit()

print(answer)