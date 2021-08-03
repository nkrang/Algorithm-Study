import sys
input = sys.stdin.readline

from collections import deque

n, m, v = map(int, input().split())
matrix = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    matrix[x][y] = matrix[y][x] = 1

def dfs(nod, passed = []):
    print(nod, end = " ")
    passed.append(nod)
    for i in range(n+1):
        if matrix[nod][i] == 1 and (i not in passed):
            dfs(i)

def bfs(nod):
    passed = []
    dq = []
    dq = deque(dq)
    passed.append(nod)
    dq.append(nod)

    while dq:
        start = dq.popleft()
        print(start, end=" ")
        for i in range(n+1):
            if matrix[start][i] == 1 and (i not in passed):
                passed.append(i)
                dq.append(i)

dfs(v)
print()
bfs(v)