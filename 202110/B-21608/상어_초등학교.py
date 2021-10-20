N = int(input())
matrix = [[0] * N for _ in range(N)]
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
bf = dict()
for k in range(N*N):
    s = list(map(int, input().split()))
    bf[s[0]] = s[1:]
    if k == 0:
        matrix[1][1] = s[0]
        continue
    res = [-1, -1]
    seat = [0, 0]
    for r in range(N):
        for c in range(N):
            b = False
            friend = 0
            empty = 0
            if matrix[r][c] == 0:
                # if seat == [0, 0] and res == [0, 0]:
                #     seat = [r, c]
                for i in range(4):
                    nr = r + dx[i]
                    nc = c + dy[i]
                    if 0 <= nr < N and 0 <= nc < N:
                        if matrix[nr][nc] in s:
                            friend += 1
                        if matrix[nr][nc] == 0:
                            empty += 1
                if friend == 4:
                    b = True
                    seat = [r, c]
                    break
                else:
                    if friend > res[0]:
                        seat = [r, c]
                        res[0] = friend
                        res[1] = empty
                    elif friend == res[0] and empty > res[1]:
                        seat = [r, c]
                        res[1] = empty
        if b:
            break
    matrix[seat[0]][seat[1]] = s[0]
answer = 0
for r in range(N):
    for c in range(N):
        f = 0
        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]
            if 0 <= nr < N and 0 <= nc < N:
                if matrix[nr][nc] in bf[matrix[r][c]]:
                    f += 1
        if f != 0:
            answer += 10 ** (f-1)

print(answer)