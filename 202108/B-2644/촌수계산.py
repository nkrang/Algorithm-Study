import sys
input = sys.stdin.readline
from collections import deque

p = int(input())
me, you = map(int, input().split())
n = int(input())

matrix = [[0] * (p+1) for _ in range(p+1)]

for _ in range(n):
    x, y = map(int, input().split())
    matrix[x][y] = matrix[y][x] = 1

res = [0] * (p+1)
passed = []
dq = [me]
dq = deque(dq)

while dq:
    allbreak = False
    start = dq.popleft()
    passed.append(start)
    for i in range(1, p+1):
        if matrix[start][i] == 1 and i not in passed:
            res[i] = res[start] + 1
            dq.append(i)
            if i == you:
                print(res[you])
                allbreak = True
                break
    if allbreak == True:
        break
else:
    print(-1)

