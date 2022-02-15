import sys
input = sys.stdin.readline

N, x, y = map(int, input().split())

arr = [x for x in range(1, N+1)]

if x > y:
    temp = x
    x = y
    y = temp

r = 0
while len(arr) > 1:
    r += 1
    temp = []
    for i in range(0, len(arr), 2):

        if i+1 < len(arr) and x == arr[i] and y == arr[i+1]:
            print(r)
            sys.exit(0)

        temp.append(arr[i])

        if x == arr[i] or (i+1 < len(arr) and x == arr[i+1]):
            x = arr[i]
        if y == arr[i] or (i+1 < len(arr) and y == arr[i+1]):
            y = arr[i]

    arr = temp[:]

if len(arr) == 1:
    print(-1)