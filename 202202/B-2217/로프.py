import sys
input = sys.stdin.readline

N = int(input())
result = 0
rope = []
for _ in range(N):
    x = int(input())
    rope.append(x)

rope.sort()
for i in range(N):
    temp = rope[i] * (N-i)
    if result <= temp:
        result = temp

print(result)