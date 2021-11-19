import sys
input = sys.stdin.readline
import heapq

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
x = [[1e9] * (N+1) for _ in range(N+1)]
result = [int(1e9)] * (N+1)
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))
    x[a][b] = c
    x[b][a] = c

result[1] = 0
answer = 0
hq = []
heapq.heappush(hq, [result[1], 1])

while hq:
    dist, nod = heapq.heappop(hq)
    if dist > result[nod]:
        continue
    for newd, newn in graph[nod]:
        newd += dist
        if newd < result[newn]:
            result[newn] = newd
            heapq.heappush(hq, [newd, newn])
            if newd < x[newn][2]:
                answer += 1
            x[newn][nod] = newd
            x[nod][newn] = newd

print(answer)