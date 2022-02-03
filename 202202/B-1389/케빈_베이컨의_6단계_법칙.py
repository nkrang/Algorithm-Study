import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [[1e9] * (N+1) for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    matrix[x][y] = 1
    matrix[y][x] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                matrix[i][j] = matrix[i][k] + matrix[k][j]

mini = 1e9
answer = 0
for i in range(1, N+1):
    x = sum(matrix[i][1:])
    if x < mini:
        answer = i
        mini = x

print(answer)