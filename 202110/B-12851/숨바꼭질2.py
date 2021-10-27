import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())

answer = 100000
time = 0

def bfs():
    global answer, time
    dq = [(N, 0)]
    dq = deque(dq)
    check = [0] * 200000
    while dq:
        me, cnt = dq.popleft()
        if me == K:
            if answer > cnt:
                answer = cnt
                time = 1
            elif answer == cnt:
                time += 1
            continue
    
        else:

            check[me] = 1
        
        if me < K:
            if check[me + 1] == 0:
                dq.append((me + 1, cnt + 1))
            if check[me * 2] == 0:
                dq.append((me * 2, cnt + 1))
        
        if me > 0:
            if check[me - 1] == 0:
                dq.append((me - 1, cnt + 1))

bfs()
print(answer)
print(time)
