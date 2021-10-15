import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
matrix = []
m = []
for i in range(R):
    line = list(map(int, input().split()))
    matrix.append(line)
    for j in range(C):
        if line[j] == -1:
            m.append((i, j))



dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def diffusion():
    temp = [[0] * C for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if matrix[x][y] > 0:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < R and 0 <= ny < C and matrix[nx][ny] != -1:
                        v = matrix[x][y] // 5
                        temp[nx][ny] += v
                        temp[x][y] -= v

    nd = []
    
    for i in range(R):
        for j in range(C):
            matrix[i][j] += temp[i][j]

    return nd


def machine():
    temp = [matrix[x][:] for x in range(R)]
    x, y = m[0]
    for i in range(2, C):
        temp[x][i] = matrix[x][i-1]
    for i in range(0, x):
        temp[i][C-1] = matrix[i+1][C-1]
    for i in range(0, C-1):
        temp[0][i] = matrix[0][i+1]
    for i in range(1, x):
        temp[i][0] = matrix[i-1][0]
    temp[x][1] = 0
    
    x, y = m[1]
    for i in range(2, C):
        temp[x][i] = matrix[x][i-1]
    for i in range(x+1, R):
        temp[i][C-1] = matrix[i-1][C-1]
    for i in range(0, C-1):
        temp[R-1][i] = matrix[R-1][i+1]
    for i in range(x+1, R-1):
        temp[i][0] = matrix[i+1][0]
    temp[x][1] = 0

    return temp

def total(matrix):
    t = 0
    for i in range(R):
        t += sum(matrix[i])
    return t

for _ in range(T):
    diffusion()
    matrix = machine()

print(total(matrix) + 2)

