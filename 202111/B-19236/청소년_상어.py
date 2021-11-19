import sys
input = sys.stdin.readline

fishloc = [0] * 17
matrix = [[0] * 4 for _ in range(4)]
for i in range(4):
    line = list(map(int, input().split()))
    for j in range(8):
        if j % 2 == 0:
            fishloc[line[j]] = (i, j//2, line[j+1])
            matrix[i][j//2] = (line[j])

dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]

sharkloc = [0, 0]
matrix[0][0] = 0

def fishmove(m, f, sx, sy):
    for i in range(len(f)):
        if f[i] == 0:
            continue
        x, y, d = f[i]
        for _ in range(8):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < 4 and 0 <= ny < 4 and (nx, ny) != (sx, sy):
                #물고기 자리 바꾸기
                temp = m[nx][ny]
                m[nx][ny] = m[x][y]
                m[x][y] = temp
                
                f[i] = (nx, ny, d)
                if temp != 0:
                    f[temp] = (x, y, f[temp][2])

                break

            d += 1
            if d == 9:
                d = 1

        print(m)
        print(f)
    
    return m, f, sx, sy
matrix, fishloc, s1, s2 = fishmove(matrix, fishloc, 0, 0)
print(matrix)
