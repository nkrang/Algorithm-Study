import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**9)

N, L, R = map(int, input().split())
matrix = []
for _ in range(N):
    line = list(map(int, input().split()))
    matrix.append(line)

chk = [[0] * N for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

res = 0

def dfs(x, y):
    print(x, y)
    global union, total, chk
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        print(nx, ny)
        if 0 <= nx < N and 0 <= ny < N and chk[nx][ny] == 0 and L <= abs(matrix[x][y] - matrix[nx][ny]) <= R:
            union.append((nx, ny))
            chk[nx][ny] = 1
            total += matrix[nx][ny]
            dfs(nx, ny)

while True:
    chk = [[0] * N for _ in range(N)]
    fin = 0
    for i in range(N):
        for j in range(N):
            print(i,j)
            if chk[i][j] == 0:
                chk[i][j] = 1
                union = [(i, j)]
                total = matrix[i][j]
                dfs(i, j)
                print(union, total)
                if len(union) < 2:
                    fin += 1
                else:
                    print("else")
                    for x, y in union:
                        matrix[x][y] = total // len(union)
                    print(matrix)
    else:
        print("fin", fin)
        if fin == N*N:
            print(res)
            break
        
        res += 1
              