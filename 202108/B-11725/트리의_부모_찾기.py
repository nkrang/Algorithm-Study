import sys
input = sys.stdin.readline
#recursion 에러 해결법
sys.setrecursionlimit(10**9)

n = int(input())

tree = [[] for _ in range(n+1)]
parent = [0] * (n+1)
for _ in range(n-1):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)

def dfs(start):
    for i in tree[start]:
        if parent[i] == 0:
            parent[i] = start
            dfs(i)

dfs(1)

for x in range(2, n+1):
    print(parent[x])