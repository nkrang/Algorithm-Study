import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

forward = [1] * n
reverse = [1] * n
both = []

for i in range(n):
    for j in range(i):
        if numbers[j] < numbers[i]:
            forward[i] = max(forward[i], forward[j] + 1)
    both.append(forward[i])

#역방향으로 for문을 돌릴 때는 -1을 써줘야 도는 구낭,,,,,,,,
for i in range(n-1, -1, -1):
    for j in range(n-1, i-1, -1):
        if numbers[j] < numbers[i]:
            reverse[i] = max(reverse[i], reverse[j] + 1)
    both[i] += reverse[i]

print(max(both) - 1)