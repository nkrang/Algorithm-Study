import sys
input = sys.stdin.readline

N = int(input())
loc = []
for i in range(N):
    loc.append(list(map(int, input().split())) + [i])

edges = []

for i in range(3):
    #적어도 한 줄은 생기니까 되는걸까..?
    #어차피 최소 간선이 이 세번 정렬 속에서 생기나보다
    temp = sorted(loc, key= lambda x: x[i])
    for j in range(1, N):
        edges.append((temp[j-1][3], temp[j][3], abs(temp[j][i] - temp[j-1][i])))

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