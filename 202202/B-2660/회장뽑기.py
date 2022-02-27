import sys
input = sys.stdin.readline

n = int(input())

matrix = [[1e9] * (n+1) for _ in range(n+1)]

while True:
    x, y = map(int, input().split())
    if x == -1 and y == -1:
        break
    matrix[x][y] = 1
    matrix[y][x] = 1

for i in range(1, n+1):
    matrix[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if matrix[i][k] + matrix[k][j] < matrix[i][j]:
                matrix[i][j] = matrix[i][k] + matrix[k][j]

result = []
num = 1e9
for i in range(1, n+1):
    m = max(matrix[i][1:])
    if m < num:
        num = m
        result = [i]
    elif m == num:
        result.append(i)

print(num, len(result))
for x in result:
    print(x, end=" ")