import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

matrix = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    if matrix[a][b] == 0 or c < matrix[a][b]:
        matrix[a][b] = c


for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j != k and matrix[i][k] != 0 and matrix[k][j] != 0:
                if matrix[i][j] == 0 or matrix[i][k] + matrix[k][j] < matrix[i][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]

for i in range(1, n+1):
    for j in range(1, n+1):
        print(matrix[i][j], end= " ")
    print()