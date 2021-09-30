import sys
input = sys.stdin.readline

n = int(input())
point = []
for _ in range(n):
    x, y = map(int, input().split())
    point.append((x, y))

for x, y in sorted(point):
    print(x, y)