import sys
input = sys.stdin.readline

n, m = map(int, input().split())
loc = []
for _ in range(n):
    loc.append(int(input()))

loc.sort()

left = 1
right = loc[-1] - loc[0]

while left <= right:
    dis = (right+left) // 2
    me = loc[0]
    cnt = 1
    for i in range(1, n):
        if me + dis <= loc[i]:
            #비교 거리보다 먼 거리에 집이 있다
            cnt += 1
            me = loc[i]
    if cnt >= m:
        #충분히 가능, 거리를 더 넓혀보자
        left = dis + 1
    else:
        #불가능, 거리를 좁혀야함
        right = dis - 1

print(left - 1)
