import sys
input = sys.stdin.readline

N, M = map(int, input().split())

matrix = []
goal = []

answer = 0

for _ in range(N):
    line = list(input().strip('\n'))
    matrix.append(line)

for _ in range(N):
    line = list(input().strip('\n'))
    goal.append(line)

def change(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            matrix[i][j] = '1' if matrix[i][j] == '0' else '0'

for i in range(N):
    for j in range(M):
        if matrix[i][j] != goal[i][j] and i <= N-3 and j <= M-3:
            change(i, j)
            answer += 1

if matrix == goal:
    print(answer)
else:
    print(-1)