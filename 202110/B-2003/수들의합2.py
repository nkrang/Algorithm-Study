import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

res = 0

for i in range(n):
    temp = numbers[i]
    for j in range(i+1, n+1):
        if temp > m:
            break
        elif temp == m:
            res += 1
            break
        if j < n:
            temp += numbers[j]

print(res)