import sys
input = sys.stdin.readline



A, B = map(int, input().split())

answer = int(1e9)
def dfs(a, cnt):
    global answer
    if a == B:
        answer = min(answer, cnt)
        return
    if a > B:
        return
    dfs(int(str(a) + '1'), cnt+1)
    dfs(a*2, cnt + 1)

dfs(A, 0)
if answer == int(1e9):
    print(-1)
else:
    print(answer+1)