from collections import deque
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def route():
    while q:
        x, y = q.popleft()
        #다른 백조와 만났다면 1 리턴
        if x == x2 and y == y2:
            return 1
        #상하좌우 값 검사
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not c[nx][ny]:
                    #들르지 않은 애들 검사
                    #얼음(갈 수 없음)이면 예비큐에, 아니면 큐에 append
                    if matrix[nx][ny] == "X":
                        temp_q.append([nx, ny])
                    else:
                        q.append([nx, ny])
                    c[nx][ny] = 1
    else:
        return 0

def melt():
    while wq:
        x, y = wq.popleft()
        #얼음 녹이기
        if matrix[x][y] == 'X':
            matrix[x][y] = "."
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not wc[nx][ny]:
                    if matrix[nx][ny] == 'X':
                        temp_wq.append([nx, ny])
                    else:
                        wq.append([nx, ny])
                    wc[nx][ny] = 1

n, m = map(int, input().split())
#백조 들렀다
c = [[0] * m for _ in range(n)]
#물 들렀다
wc = [[0] * m for _ in range(n)]

q, temp_q, wq, temp_wq = deque(), deque(), deque(), deque()

#좌표값 입력 받으면서 물(.) 지나갈 수 있는 좌표 wq큐에 입력
matrix, swan = [], []
for i in range(n):
    row = list(input().strip('\n'))
    matrix.append(row)
    for j, k in enumerate(row):
        if matrix[i][j] == 'L':
            swan.extend([i, j])
            wq.append([i, j])
        elif matrix[i][j] == ".":
            wc[i][j] = 1
            wq.append([i, j])
        
#백조 좌표
x1, y1, x2, y2 = swan
#q큐에 시작 백조 좌표 넣고 들렀다 값 1로
q.append([x1, y1])
c[x1][y1] = 1
cnt = 0

while True:
    #녹이기 실행
    melt()
    #route함수 리턴 값이 1이면 백조가 만난거
    if route():
        print(cnt)
        break
    #예비큐 값을 큐로 옮기고 예비 큐는 비운 뒤 다시 실행
    q = temp_q
    wq = temp_wq
    temp_q, temp_wq = deque(), deque()
    cnt += 1