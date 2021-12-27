import sys
input = sys.stdin.readline

R, C = map(int, input().split())
matrix = []
for _ in range(R):
    line = list(input().strip('\n'))
    matrix.append(line)

d = [(-1, 1), (0, 1), (1, 1)]
visited = [[0] * C for _ in range(R)]
answer = 0
check = [0] * R

def dfs(no, r, c, temp):
    global answer
    #temp.append((r, c))
    if check[no] == 1:
        return
    if c == C-1:
        check[no] = 1
        # for x, y in temp:
        #     visited[x][y] = 1
        answer += 1
        return
    for i in range(3):
        nr = r + d[i][0]
        nc = c + d[i][1]
        if 0 <= nr < R and 0 <= nc < C and visited[nr][nc] == 0 and matrix[nr][nc] != 'x':
            dfs(no, nr, nc, temp)
    


for i in range(R):
    dfs(i, i, 0, [])

print(answer)