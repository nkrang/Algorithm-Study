import sys
input = sys.stdin.readline

n, m = map(int, input().split())
visited = []

def bt():
    if len(visited) == m:
        for x in visited:
            print(x, end=" ")
        print()
        return

    else:
        for i in range(1, n+1):
            if i not in visited:
                visited.append(i)
                bt()
                visited.pop()

bt()