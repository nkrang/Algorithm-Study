import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())
rx, ry, rz = list(map(int, input().split()))
matrix = []
for _ in range(n):
    line = list(map(int, input().split()))
    matrix.append(line)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 1

def dfs(x, y, z, temp): #좌표, 방향
    global cnt, matrix
    if matrix[x][y] == 0:
        matrix[x][y] = -1
    if z-1 < 0:
        z = 3
    else:
        z -= 1
    lx = x + dx[z]
    ly = y + dy[z]
    if matrix[lx][ly] == 0:
        #왼쪽으로 이동
        temp = []
        cnt += 1
        dfs(lx, ly, z, temp)
        return
    else:
        #네방향 다 체크
        if len(temp) == 3:
            bx = x + dx[z-2]
            by = y + dy[z-2]
            if 0 <= bx < n and 0 <= by < m and matrix[bx][by] == 1:
                #끝
                print(cnt)
                sys.exit(0)
            else:
                #후진
                temp = []
                dfs(bx, by, z, temp)
        else:
            temp.append(1)
            
            dfs(x, y, z, temp)

temp = []
dfs(rx, ry, rz, temp)