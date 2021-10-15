import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
matrix = []
px, py = 0, 0
size, eat = 2, 0
time = 0

for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] == 9:
            px, py = i, j
    matrix.append(line)
    

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]  

matrix[px][py] = 0


def move():
    global px, py, fish, size, eat, time
    check = [[0] * n for _ in range(n)]
    dq = deque([(px, py, 0)])
    check[px][py] = 1
    distance = 0
    prey = []
    while dq:
        #print(dq)
        x, y, cnt = dq.popleft()
        if len(prey) != 0 and cnt > distance:
            break
        elif len(prey) == 0 and cnt > distance:
            distance = cnt

        if 0 < matrix[x][y] < size:
            prey.append((x, y))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and check[nx][ny] == 0 and matrix[nx][ny] <= size:
                check[nx][ny] = 1
                dq.append((nx, ny, cnt + 1))
    
    if len(prey) != 0:
        prey.sort()
    
        px, py = prey[0]
        time += distance
        matrix[px][py] = 0
        eat += 1
    else:
        print(time)
        sys.exit(0)
    

while True:
    move()
    if size == eat:
        size += 1
        eat = 0

