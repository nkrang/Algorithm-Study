import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**5)

N, Q = map(int, input().split())
N = 2 ** N
matrix = []
for _ in range(N):
    line = list(map(int, input().split()))
    matrix.append(line)

L = list(map(int, input().split()))

def storm(l):
    temp = [[0] * N for _ in range(N)]
    for x in range(0, N, l):
        for y in range(0, N, l):
            for i in range(x, x+l):
                for j in range(y, y+l):
                    ti = i - x
                    tj = j - y
                    temp[x + j - y][y + l - 1 - ti] = matrix[i][j]
                    #temp[x + j][y + l - 1 - i] = matrix[i][j]
    return temp

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def melt():
    temp = [[0] * N for _ in range(N)]
    total = 0
    for x in range(N):
        for y in range(N):
            cnt = 0
            if matrix[x][y] > 0:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < N and 0 <= ny < N and matrix[nx][ny] > 0:
                        cnt += 1
                if cnt < 3:
                    temp[x][y] = matrix[x][y] - 1
                else:
                    temp[x][y] = matrix[x][y]
                total += temp[x][y]

    return temp, total

check = [[0] * N for _ in range(N)]
def bigIce(x, y):
    big = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and check[nx][ny] == 0 and matrix[nx][ny] > 0:
            check[nx][ny] = 1
            big += bigIce(nx, ny)
    return big

def printmatrix():
    for x in matrix:
        print(x)

for i in L:
    matrix = storm(2 ** i)
    matrix, ans = melt()

res = 0
for i in range(N):
    for j in range(N):
        if matrix[i][j] > 0 and check[i][j] == 0:
            check[i][j] = 1
            res = max(res, bigIce(i, j))

print(ans)
print(res)