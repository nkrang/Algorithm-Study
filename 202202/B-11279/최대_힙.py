import sys
input = sys.stdin.readline
import heapq as hq

N = int(input())

h = []
for _ in range(N):
    x = int(input())
    if x == 0:
        if h:
            print(-hq.heappop(h))
        else:
            print(0)
    else:
        hq.heappush(h, -x)