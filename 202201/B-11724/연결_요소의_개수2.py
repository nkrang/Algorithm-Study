import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
edges = [[] for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    edges[x].append(y)
    edges[y].append(x)

visited = [0] * (N+1)

def bfs(nod):
    visited[nod] = 1
    dq = deque([nod])
    while dq:
        x = dq.popleft()
        for i in edges[x]:
            if visited[i] == 0:
                dq.append(i)
                visited[i] = 1

answer = 0
for i in range(1, N+1):
    if visited[i] == 0:
        bfs(i)
        answer += 1

print(answer)