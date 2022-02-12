import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
matrix = []
for _ in range(N):
    line = list(map(int, input().strip('\n')))
    matrix.append(line)

visited = [[0] * M for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

result = 0
def bfs(x, y, h):
    #x, y에서 시작해서 높이 h 이하안에 있는 그룹 찾기
    global result
    cnt = 1
    dq = deque([(x, y)])
    visited[x][y] = 1
    flag = True
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                #높이 h이하 안에 있는 경우만 물 +1 
                if visited[nx][ny] == 0 and matrix[nx][ny] <= h:
                    visited[nx][ny] = 1
                    dq.append((nx, ny))
                    cnt += 1
            else:
                #범위 밖으로 나가면 물이 흘러서 안됨
                flag = False
                continue
    #물이 흐른 적 없는 애들만
    if flag:
        result += cnt

#물이 1에서 8까지 가능하므로 한 단계씩 체크
for h in range(1, 9):
    visited = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and matrix[i][j] <= h:
                bfs(i, j, h)

print(result)