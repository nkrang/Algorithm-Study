import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
matrix = []
for _ in range(N):
    line = list(map(int, input().split()))
    matrix.append(line)

air = [[0] * M for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

#속에 있는 빈칸은 공기가 아니고 겉에 있는 큰 한 덩어리 빈칸만 공기기 때문에 bfs돌면서 큰 한 덩어리 공기만 검사한다.
def checkAir():
    temp = []
    visited = [[0] * M for _ in range(N)]
    dq = deque([(0, 0)])
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            #1이면 공기와 닿은 치즈이기 때문에 녹일 배열에 넣고
            #0이면 dq에 넣어서 계속 검사를 진행한다.
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] == 1:
                    temp.append((nx, ny))
                else:
                    dq.append((nx, ny))
                visited[nx][ny] = 1

    return temp

result = 0
turn = 0
while True:
    #위의 함수를 실행해서 녹일 배열을 받아온다
    toMelt = checkAir()
    #녹일 치즈가 없으면 출력 후 break
    if len(toMelt) == 0:
        print(turn)
        print(result)
        break

    result = len(toMelt)
    turn += 1

    #melt
    for x, y in toMelt:
        matrix[x][y] = 0