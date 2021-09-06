import sys
input = sys.stdin.readline
from collections import deque


def bfs():
    while dq:
        x, y = dq.popleft()
        if x == gx and y == gy:
            print("happy")
            break
        else:
            for s in graph:
                dis = abs(s[0] - x) + abs(s[1] - y)
                if dis <= 1000 and s not in passed:
                    dq.append(s)
                    passed.append(s)
    else:
        print("sad")

n = int(input())
for _ in range(n):
    passed = []
    m = int(input())
    graph = []
    hx, hy = map(int, input().split())
    for _ in range(m):
        x, y = map(int, input().split())
        graph.append((x, y))
    gx, gy = map(int, input().split())
    graph.append((gx, gy))
    dq = [(hx, hy)]
    dq = deque(dq)
    bfs()
