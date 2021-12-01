import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    matrix[y][x] = -1
    matrix[x][y] = 1

result = [0] * (N+1)

answer = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if matrix[i][k] != 0 and matrix[k][j] == matrix[i][k]:
                matrix[i][j] = matrix[i][k]
                matrix[j][i] = -matrix[i][k]
                result[i] += 1
                if result[i] == N-1:
                    answer += 1
                    break

print(answer)