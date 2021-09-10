import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

tree = [[] for _ in range(n)]

for _ in range(n-1):
    x, y, z = list(map(int, input().split()))
    tree[x-1].append([z, y-1])
    tree[y-1].append([z, x-1])

def line_length(x, mode):
    q = [x]
    q = deque(q)
    value = [-1] * n
    value[x] = 0
    while q:
        nod = q.popleft()
        for w, nx in tree[nod]:
            if value[nx] == -1:
                q.append(nx)
                value[nx] = value[nod] + w

    if mode == 1:
        return value.index(max(value))
    else:
        return max(value)
    
print(line_length(line_length(0, 1), 2))

#솔직히 전혀 모르겟음