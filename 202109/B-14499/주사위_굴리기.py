import sys
input = sys.stdin.readline

#밑북서위남동
dice = [0] * 6

def rollDice(d, dice):
    temp = dice[:]
    cross = [0, 2, 3, 5]
    col = [0, 1, 3, 4]
    if d == 1:
        for i in range(4):
            dice[cross[i]] = temp[cross[i-1]]
    elif d == 2:
        for i in range(4):
            dice[cross[i-1]] = temp[cross[i]]
    elif d == 3:
        for i in range(4):
            dice[col[i]] = temp[col[i-1]]
    elif d == 4:
        for i in range(4):
            dice[col[i-1]] = temp[col[i]]

N, M, x, y, n = map(int, input().split())
matrix = []
for _ in range(N):
    line = list(map(int, input().split()))
    matrix.append(line)
move = list(map(int, input().split()))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for m in move:
    
    nx = x + dx[m-1]
    ny = y + dy[m-1]
    if 0 <= nx < N and 0 <= ny < M:
        x = nx
        y = ny
        rollDice(m, dice)
        if matrix[x][y] == 0:
            matrix[x][y] = dice[0]
        else:
            dice[0] = matrix[x][y]
            matrix[x][y] = 0
        print(dice[3])