import sys
input = sys.stdin.readline

n = int(input().strip('\n'))
cnt = 0
temp = n
while temp > 0:
    temp = temp//10
    cnt += 1

x = n - 9 * cnt

while x < n:
    temp = x
    first = n
    while temp > 0:
        num = temp % 10
        first = first - num
        temp = temp//10
    if first == x:
        print(x)
        break
    else:
        x = x + 1
else:
    print(0)