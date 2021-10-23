fishloc = [0] * 17
matrix = [[0] * 4 for _ in range(4)]
for i in range(4):
    line = list(map(int, input().split()))
    for j in range(8):
        if j % 2 == 0:
            fishloc[line[j]] = (i, j//2)
            matrix[i][j//2] = (line[j], line[j+1])

dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]

res = 0


def fishmove(matrix, fishloc):
    for i in range(1, 17):
        if fishloc[i] == -1:
            continue
        x, y = fishloc[i]
        d = matrix[x][y][1]
        while True:
            nx = x + dx[d]
            ny = y + dy[d]
            # 경계를 넘거나 상어가 아니면
            if 0 <= nx < 4 and 0 <= ny < 4:
                if matrix[nx][ny][0] != 0:
                    if matrix[nx][ny] != (-1, -1):
                        fishloc[matrix[nx][ny][0]] = (x, y)
                    fishloc[matrix[x][y][0]] = (nx, ny)
                    temp = matrix[nx][ny]
                    matrix[nx][ny] = (matrix[x][y][0], d)
                    matrix[x][y] = temp
                break
            else:
                d += 1
                if d > 8:
                    d = 1
    return matrix, fishloc


result = 0
def sharkmove():
    global result
    m, l, p = dq.pop(0)
    m, l = fishmove(m, l)
    result = max(result, p)
    print("1)", p)
    print(m)
    x, y = l[0]
    d = m[x][y][1]
    m[x][y] = (-1, -1)
    while True:
        x += dx[d]
        y += dy[d]
        nm = [[x for x in y] for y in m]
        nl = l[:]
        if 0 <= x < 4 and 0 <= y < 4:
            if nm[x][y][1] != -1:
                nl[0] = (x, y)
                eaten = nm[x][y][0]
                nl[eaten] = -1
                nm[x][y] = (0, nm[x][y][1])
                dq.append((nm, nl, p + eaten))
                print("2)", p+eaten)
        else:
            break

fishloc[0] = (0, 0)
first = matrix[0][0][0]
fishloc[first] = -1
matrix[0][0] = (0, matrix[0][0][1])
dq = []
dq.append((matrix, fishloc, first))

while dq:
    sharkmove()

print(result)