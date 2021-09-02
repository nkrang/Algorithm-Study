import sys
input = sys.stdin.readline

m, n, h = map(int, input().split())

box = []
unripe = 0

for _ in range(h):
    floor = []
    for _ in range(n):
        line = list(map(int, input().split()))
        unripe += line.count(0)
        floor.append(line)
    box.append(floor)


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

res = 0

while True:
    will = []
    for f in range(h):
        for x in range(n):
            for y in range(m):
                if box[f][x][y] == 1:
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if 0 <= nx < n and 0 <= ny < m and box[f][nx][ny] == 0:
                            will.append((f, nx, ny))
                    if f+1 < h and box[f+1][x][y] == 0:
                        will.append((f+1, x, y))
                    if f-1 >= 0 and box[f-1][x][y] == 0:
                        will.append((f-1, x, y))
    will = set(will)
    unripe -= len(will)
    if len(will) == 0:
        if unripe == 0:
            print(res)
        else:
            print(-1)
        break
    for x in will:
        box[x[0]][x[1]][x[2]] = 1
    res += 1
