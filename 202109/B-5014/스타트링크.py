import sys
input = sys.stdin.readline
from collections import deque

F, S, G, U, D = map(int, input().split())

dq = [S]
dq = deque(dq)
passed = [-1] * (F+1)
passed[S] = 0

move = [U, -1 * D]

while dq:
    now = dq.popleft()
    if now == G:
        print(passed[G])
        break
    for i in range(2):
        moved = now + move[i]
        if 0 < moved <= F and passed[moved] == -1:
            dq.append(moved)
            passed[moved] = passed[now] + 1
else:
    print("use the stairs")