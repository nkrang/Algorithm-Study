import sys
input = sys.stdin.readline

T = int(input())
parent = []
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

for _ in range(T):
    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        x, y = map(int, input().split())
        edges.append((x, y))

    
    parent = [x for x in range(N+1)]
    answer = 0

    for x, y in edges:
        if parent[x] != parent[y]:
            answer += 1
            union_parent(x, y)
    print(answer)
