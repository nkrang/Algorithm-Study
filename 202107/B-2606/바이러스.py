import sys
input = sys.stdin.readline

computer = int(input())
connection = int(input())
virus = []

for _ in range(connection):
    n, m = map(int, input().split())
    virus.append((n, m))

visited = [1]

def dfs(nod):
    for x in virus:
        if nod == x[0] and x[1] not in visited:
            visited.append(x[1])
            dfs(x[1])
        elif nod == x[1] and x[0] not in visited:
            visited.append(x[0])
            dfs(x[0])

dfs(1)
print(len(visited)-1)