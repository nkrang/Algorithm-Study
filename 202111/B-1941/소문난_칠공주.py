import sys
input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

matrix = []
visited = [[0] * 5 for _ in range(5)]

answer = 0

def dfs(x, y, cnt, yn):
    global visited, answer
    visited[x][y] = 1
    if cnt == 7:
        answer += 1
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5 and visited[nx][ny] == 0:
            if matrix[nx][ny] == 'Y':
                if yn < 3:
                    dfs(nx, ny, cnt+1, yn+1)
                else:
                    return
            else:
                dfs(nx, ny, cnt+1, yn)

for _ in range(5):
    line = list(input().strip('\n'))
    matrix.append(line)


for i in range(5):
    for j in range(5):
        visited = [[0] * 5 for _ in range(5)]
        if matrix[i][j] == 'Y':
            dfs(i, j, 1, 1)
        else:
            dfs(i, j, 1, 0)

print(answer)
            