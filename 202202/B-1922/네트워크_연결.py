import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
edges = []
for _ in range(M):
    edges.append(list(map(int, input().split())))

edges = sorted(edges, key= lambda x:x[2])
parent = [x for x in range(N+1)]

def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

answer = 0
for x, y, c in edges:
    if find_parent(x) != find_parent(y):
        union_parent(x, y)
        answer += c

print(answer)