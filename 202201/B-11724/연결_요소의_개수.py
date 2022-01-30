N, M = map(int, input().split())
edges = []
for _ in range(M):
    x, y = map(int, input().split())
    edges.append((x, y))

parent = [x for x in range(N+1)]

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

answer = 0
for a, b in sorted(edges):
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)

print(len(set(parent)) - 1)
