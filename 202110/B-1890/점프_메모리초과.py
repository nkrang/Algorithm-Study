import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
matrix = []
for _ in range(n):
    line = list(map(int, input().split()))
    matrix.append(line)

dq = deque([(0, 0)])

ans = 0

while dq:
    x, y = dq.popleft()
    if x == n-1 and y == n-1:
        ans += 1
        continue
    size = matrix[x][y]
    if y+size < n:
        dq.append((x, y+size))
    if x+size < n:
        dq.append((x+size, y))

print(ans)
    
