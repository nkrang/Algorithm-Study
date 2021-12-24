import sys
import heapq
input = sys.stdin.readline

V = int(input())
E = int(input())
graph = [[] for _ in range(V + 1)]
distance = [1e9] * (V+1)
heap = []


for _ in range(E):
    x, y, z = map(int, input().split())
    graph[x].append([z, y])

S, G = map(int, input().split())

def Dijkstra(start):
    distance[start] = 0
    heapq.heappush(heap, [0, start])

    while heap:
        w, n = heapq.heappop(heap)

        if distance[n] < w:
            continue

        for nw, nn in graph[n]:
            next_w = nw + w
            if next_w < distance[nn]:
                distance[nn] = next_w
                heapq.heappush(heap, [next_w, nn])

Dijkstra(S)
print(distance[G])