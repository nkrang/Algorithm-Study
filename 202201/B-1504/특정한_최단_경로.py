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

distance = [[1e9] * 3 for _ in range(N+1)]

def Dijkstra():
    temp = []
    if 1 in must:
        temp.append(1)
    heap = []
    hq.heappush(heap, (0, 1, temp))

    distance[1][len(temp)] = 0

    while heap:
        print(heap)
        w, n, m = hq.heappop(heap)
        if distance[n][len(m)] < w:
            continue

        for nw, nn in matrix[n]:
            nm = m[:]
            next_w = w + nw
            if nn in must and nn not in nm:
                if distance[nn][len(nm) + 1] > next_w:
                    nm.append(nn)
                    distance[nn][len(nm)] = next_w
                    hq.heappush(heap, (next_w, nn, nm))
            else:
                if distance[nn][len(nm)] > next_w:
                    distance[nn][len(nm)] = next_w
                    hq.heappush(heap, (next_w, nn, nm))

    print(distance)
    if distance[N][2] >= 1e9:
        print(-1)
    else:
        print(distance[N][2])

Dijkstra()

