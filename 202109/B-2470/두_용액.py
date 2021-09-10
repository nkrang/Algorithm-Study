import sys
input = sys.stdin.readline

n = int(input())
acid = list(map(int, input().split()))
acid.sort()

left = 0
right = n-1

mini = 2000000000
x, y = 0, 0

while left < right:
    left_value = acid[left]
    right_value = acid[right]

    total = left_value + right_value
    if abs(total) < mini:
        mini = abs(total)
        x = left_value
        y = right_value

    if mini == 0:
        break

    if total < 0:
        left += 1
    else:
        right -= 1

print(x, y)