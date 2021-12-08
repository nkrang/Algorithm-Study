import sys
input = sys.stdin.readline

n = int(input())
size = list(map(str, input().split()))

maxi = ""
mini = ""

visited = [0] * 10

def check(mark, x, y):
    if mark == '<':
        return x<y
    else:
        return x>y
    

def dfs(idx, s):
    global maxi, mini
    if idx == n+1:
        if len(mini) == 0:
            mini = s
        else:
            maxi = s
        return

    for i in range(10):
        if visited[i] == 0:
            if idx == 0 or check(size[idx-1], int(s[-1]), i):
                visited[i] = 1
                dfs(idx+1, s+str(i))
                visited[i] = 0

dfs(0, "")
print(maxi)
print(mini)