import sys
input = sys.stdin.readline

n = int(input())
table = []
visited = [[0] * n for i in range(n)]

for _ in range(n):
    line = input().strip('\n')
    table.append(list(map(int, line)))

#상하좌우 확인용
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    visited[x][y] = 1
    global nums
    if table[x][y] == 1:
        nums += 1
        for i in range(4):
            #상하좌우 확인
            nx = x + dx[i]
            ny = y + dy[i]
            #상하좌우가 0 ~ n이고 방문 안했고, 아파트 있으면 재귀 호출
            if 0 <= nx and nx < n and 0 <= ny and ny < n:
                if visited[nx][ny] == 0 and table[nx][ny] == 1:
                    dfs(nx, ny)

answer = []
nums = 0

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and table[i][j] == 1:
            #table 값이 1이므로 dfs 호출. 
            #상하좌우 검사하면서 수 세기
            dfs(i, j)
            answer.append(nums)
            nums = 0

print(len(answer))
answer.sort()
for x in answer:
    print(x)

                