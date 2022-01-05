import sys
input = sys.stdin.readline

N, L = map(int, input().split())
pond = []
for _ in range(N):
    x, y = map(int, input().split())
    pond.append((x, y))

answer = 0
last = 0
pond.sort()
for x, y in pond:
    if x < last:
        x = last
    temp = (y-x) / L
    if temp % 1 != 0:
        temp += 1
    temp = int(temp)
    answer += temp

    last = x + temp* L

print(answer)