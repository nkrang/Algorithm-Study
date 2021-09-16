import sys
input = sys.stdin.readline
n, m = map(int, input().split())
matrix = []
for _ in range(n):
    line = list(map(int, input().split()))
    matrix.append(line)

dx = [1, 0]
dy = [0, 1]

ans = 0

def dfs(x, y, chosen, passed):
    global ans
    print(x, y, chosen)
    if len(chosen) == 4:
        ans = max(ans, sum(chosen))
        print(chosen, ans)
        return

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in passed:
            dfs(nx, ny, chosen + [matrix[nx][ny]], passed + [(nx, ny)])

for i in range(n):
    for j in range(m):
        dfs(i, j, [matrix[i][j]], [(i, j)])
print(ans)