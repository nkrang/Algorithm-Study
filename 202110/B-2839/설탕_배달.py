import sys
input = sys.stdin.readline

N = int(input())
res = N
for x in range(0, N//5 + 1):
    bag = x
    y = N - 5 * x
    if y % 3 == 0:
        bag += y // 3
        res = min(res, bag)
    else:
        continue

if res == N:
    print(-1)
else:
    print(res)