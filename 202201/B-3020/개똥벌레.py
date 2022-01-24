import sys
input = sys.stdin.readline

N, H = map(int, input().split())
arr = [0] * H
for i in range(N):
    x = int(input())
    if i % 2 == 0:
        #석순
        arr[0] += 1
        arr[x] -= 1
    else:
        #종유석
        arr[-x] += 1

now = 0
for i in range(H):
    now += arr[i]
    arr[i] = now
temp = min(arr)
print(temp, arr.count(temp))