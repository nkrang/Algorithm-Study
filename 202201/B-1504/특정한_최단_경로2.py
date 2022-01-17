import sys
input = sys.stdin.readline
import heapq as hq

N, E = map(int, input().split())
matrix = [[] for _ in range(N+1)]
for _ in range(E):
    x, y, z = map(int, input().split())
    matrix[x].append((z, y))
    matrix[y].append((z, x))

must = list(map(int, input().split()))


def Dijkstra(start):

    distance = [1e9] * (N+1)
    heap = []
    hq.heappush(heap, (0, start))
    distance[start] = 0

    while heap:
        w, n = hq.heappop(heap)
        if distance[n] < w:
            continue

        for nw, nn in matrix[n]:
            next_w = w + nw
            if distance[nn] > next_w:
                distance[nn] = next_w
                hq.heappush(heap, (next_w, nn))

    return distance

D1 = Dijkstra(1)
D2 = Dijkstra(must[0])
D3 = Dijkstra(must[1])
#1 -> v1 -> v2 -> N
#1 -> v2 -> v1 -> N
value1 = D1[must[0]] + D2[must[1]] + D3[N]
value2 = D1[must[1]] + D3[must[0]] + D2[N]

answer = min(value1, value2) if min(value1, value2) < 1e9 else -1
print(answer)


