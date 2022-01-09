import sys
import heapq as hq
input = sys.stdin.readline

V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
dist = [[1e9] * (V+1) for _ in range(V+1)]

heap = []
for _ in range(E):
    x, y, c = map(int, input().split())
    graph[x].append([c, y])
    dist[x][y] = c
    hq.heappush(heap, [c, x, y])


while heap:
    d, s, g = hq.heappop(heap)
    #heap을 쓰면 d가 가장 작은 순으로 정렬되기 때문에
    #s == g인 경우 출발지에서 출발해 다시 출발지로 돌아온 경우 = 사이클
    #사이클을 돈 가장 최소 비용이 d
    #이 부분에서 시간을 많이 단축할 수 있음
    if s == g:
        print(d)
        break
    if dist[s][g] < d:
        continue
    for nd, ng in graph[g]:
        new_d = d + nd
        if new_d < dist[s][ng]:
            dist[s][ng] = new_d
            hq.heappush(heap, [new_d, s, ng])
else:
    print(-1)
