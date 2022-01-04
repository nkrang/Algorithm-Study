import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic = {x:[] for x in range(N)}
for _ in range(M):
    x, y = map(int, input().split())
    dic[x].append(y)
    dic[y].append(x)

visited = [False] * N

answer = 0

def dfs(nod, depth):
    global answer
    if depth == 4:
        answer = 1
        return
    for x in dic[nod]:
        if visited[x] == False:
            visited[x] = True
            dfs(x, depth+1)
            visited[x] = False

for i in range(N):
    if answer == 1:
        break
    visited[i] = True
    dfs(i, 0)
    visited[i] = False

print(answer)