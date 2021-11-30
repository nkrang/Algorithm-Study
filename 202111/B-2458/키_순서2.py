import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [[[] for _ in range(2)] for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    matrix[x][1].append(y)
    matrix[y][0].append(x)

check = set()

def dfs(nod):
    global big, small
    for i in matrix[nod][0]:
        check.add(i)
        dfs(i)
    for i in matrix[nod][1]:
        check.add(i)
        dfs(i)

answer = 0
for i in range(1, N+1):
    check = set()
    dfs(i)
    if len(check) == N-1:
        answer += 1

print(answer)

