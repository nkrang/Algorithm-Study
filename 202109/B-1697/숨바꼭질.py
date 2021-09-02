import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())

limit = 100001
passed = [0] * limit 
dq = [n]
dq = deque(dq)

res = 0

while dq:
    now = dq.popleft()
    if now == k:
        break
    temp = [now+1, now-1, now*2]
    for x in temp:
        if 0 <= x < 100001 and passed[x] == 0:
            dq.append(x)
            passed[x] = passed[now] + 1

print(passed[k])


#limit를 지정해주지 않으면 메모리초과가,,,!!!!!!ㅠㅠ
#문제에서 주어진 n과 k의 위치가 0~100000 사이이므로 그만큼의 리미트를 정해주자
#-로 내려가면 어차피 *2 연산이 안통하기 때문에 -로 내려가는 경우는 최소값이라고 볼 수 없음
#100000이 넘어가는 경우도 마찬가지