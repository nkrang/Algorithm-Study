import sys
input = sys.stdin.readline

n = int(input())
time = []
for _ in range(n):
    x, y = map(int, input().split())
    time.append((x, y))

time = sorted(time, key=lambda x: x[0])
time = sorted(time, key=lambda x: x[1])

last = 0
cnt = 0

for x, y in time:
    if x >= last:
        cnt += 1
        last = y

print(cnt)