import sys
input = sys.stdin.readline

N, M = map(int, input().split())

matrix = []
for _ in range(N):
    line = list(map(int, input().split()))
    matrix.append(line)

cloud = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]




def move(d, s):
    dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
    dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]
    new = []
    global cloud
    for v in cloud:
        x, y = v
        nx = x + dx[d] * s
        ny = y + dy[d] * s
        if nx >= N:
            nx = nx % N
        if nx < 0:
            while nx < 0:
                nx += N
        if ny >= N:
            ny = ny % N
        if ny < 0:
            while ny < 0:
                ny += N
        new.append((nx, ny))
    return new



def bibaragi():
    dx = [-1, -1, 1, 1]
    dy = [-1, 1, -1, 1]
    global cloud
    for v in cloud:
        x, y = v
        matrix[x][y] += 1
    
    for v in cloud:
        x, y = v
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and matrix[nx][ny] > 0:
                matrix[x][y] += 1
    
    new = []
    total = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] >= 2 and (i, j) not in cloud:
                new.append((i, j))
                matrix[i][j] -= 2
            total += matrix[i][j]

    return new, total

ans = 0
for _ in range(M):
    d, s = map(int, input().split())
    cloud = move(d, s)
    cloud, ans = bibaragi()
print(ans)