from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    num, file = map(int, input().split())
    temp = list(map(int, input().split()))
    majority = []
    cnt = 1
    for i in range(num):
        majority.append((temp[i], i))
    majority = deque(majority)
    while majority:
        if max(majority)[0] == majority[0][0]:
            x = majority.popleft()
            if x[1] == file:
                print(cnt)
                break
            else:
                cnt += 1
        else:
            x = majority.popleft()
            majority.append(x)