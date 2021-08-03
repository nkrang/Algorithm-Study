import sys
input = sys.stdin.readline

n, m = map(int, input().split())
visited = []

def bf():
    if len(visited) == m:
        for x in visited:
            print(x, end=" ")
        print()
        return
    else:
        for i in range(1, n+1):
            if len(visited) == 0 or visited[-1] < i:
                visited.append(i)
                bf()
                visited.pop()

bf()