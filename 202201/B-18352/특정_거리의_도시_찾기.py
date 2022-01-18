import sys
input = sys.stdin.readline
import heapq as hq

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)

dist = [1e9] * (N+1)
heap = []
hq.heappush(heap, (0, X))
dist[X] = 0
while heap:
    w, n = hq.heappop(heap)
    if dist[n] < w:
        continue
    for nn in graph[n]:
        next_w = w + 1
        if dist[nn] > next_w:
            dist[nn] = next_w
            hq.heappush(heap, (next_w, nn))

result = []
for i in range(1, N+1):
    if dist[i] == K:
        result.append(i)

if result:
    for x in result:
        print(x)
else:
    print(-1)