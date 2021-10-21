from collections import deque
N, M = map(int, input().split())
matrix = []
for _ in range(N):
    line = list(map(int, input().split()))
    matrix.append(line)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def dfs(dq, check, color):
    group = []
    rainbow = 0
    mainx, mainy = dq[0][0], dq[0][1]
    while dq:
        x, y = dq.popleft()
        if matrix[x][y] == 0:
            rainbow += 1
        group.append((x, y))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and check[nx][ny] == 0 and matrix[nx][ny] >= 0:
                if color == -1:
                    if matrix[nx][ny] > 0:
                        color = matrix[nx][ny]
                    dq.append((nx, ny))
                    check[nx][ny] = 1
                else:
                    if matrix[nx][ny] == 0 or matrix[nx][ny] == color:
                        dq.append((nx, ny))
                        check[nx][ny] = 1
    if group.count(0) == len(group):
        return [], -1, 1000000, 1000000
    else:
        return group, rainbow, mx, my

# def gravity():
#     for i in range(N):
#         floor = N
#         fall = 0
#         for j in range(N-1, -1, -1):
#             if floor != N and matrix[j][i] >= 0 and j < floor:
#                 matrix[floor][i] = matrix[j][i]
#                 matrix[j][i] = -2
#                 floor = j
#
#             if matrix[j][i] == -1:
#                 floor = N
#
#             if floor == N and matrix[j][i] == -2:
#                 floor = j

# 중력 함수
def gravity(a):
    for i in range(N-2, -1, -1):  # 밑에서 부터 체크
        for j in range(N):
            if a[i][j] > -1:  # -1이 아니면 아래로 다운
                r = i
                while True:
                    if 0<=r+1<N and a[r+1][j] == -2:  # 다음행이 인덱스 범위 안이면서 -2이면 아래로 다운
                        a[r+1][j] = a[r][j]
                        a[r][j] = -2
                        r += 1
                    else:
                        break

answer = 0
while True:
    dq = deque()
    check = [[0] * N for _ in range(N)]
    maxi = []
    maxr = -1
    maxix, maxiy = 1000000, 1000000
    for i in range(N):
        for j in range(N):
            if check[i][j] == 0 and matrix[i][j] > -1:
                dq.append((i, j))
                g = []
                r = 0
                mx, my = 0, 0
                check[i][j] = 1
                if matrix[i][j] > 0:
                    g, r, mx, my = dfs(dq, check, matrix[i][j])
                else:
                    g, r, mx, my = dfs(dq, check, -1)

                if len(g) > len(maxi):
                    maxi, maxr, maxix, maxiy = g, r, mx, my
                elif len(g) == len(maxi):
                    if r > maxr:
                        maxi, maxr, maxix, maxiy = g, r, mx, my
                    elif r == maxr:
                        if mx < maxix:
                            maxi, maxr, maxix, maxiy = g, r, mx, my
                        elif mx == maxix:
                            if my < maxiy:
                                maxi, maxr, maxix, maxiy = g, r, mx, my

    if len(maxi) <= 1:
        break
    print(maxi)
    for x, y in maxi:
        matrix[x][y] = -2

    answer += len(maxi) ** 2

    #중력
    gravity(matrix)
    print(matrix)
    #회전
    matrix = list(zip(*matrix))[::-1]
    for i in range(N):
        matrix[i] = list(matrix[i])
    #중력
    gravity(matrix)
    print(matrix)

print(answer)