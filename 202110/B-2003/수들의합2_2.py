import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

res = 0

left = 0
right = 1
temp = numbers[left]

while left < n:
    if temp == m:
        temp -= numbers[left]
        left += 1
        res += 1
    elif temp > m:
        temp -= numbers[left]
        left += 1
    elif temp < m:
        temp += numbers[right]
        right += 1
    if right == n and temp < m:
        break


print(res)