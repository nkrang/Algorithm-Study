import sys
input = sys.stdin.readline
import heapq as hq

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    x, y, c = map(int, input().split())
    graph[x].append((c, y))


def Dijkstra(start):
    distance = [1e9] * (N+1)
    distance[start] = 0
    heap = []
    hq.heappush(heap, (0, start))

    while heap:
        w, n = hq.heappop(heap)

        if distance[n] < w:
            continue
        for nw, nn in graph[n]:
            next_w = nw + w
            if next_w < distance[nn]:
                distance[nn] = next_w
                hq.heappush(heap, (next_w, nn))

    return distance

answer = 0
for i in range(1, N+1):
    if i == X:
        continue
    #i->X 갔다가 X->i 돌아오기
    temp = Dijkstra(i)[X] + Dijkstra(X)[i]
    answer = max(answer, temp)

print(answer)