import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr.sort()
answer = 0

s, e = 0, n-1

print(arr)
while s < e:
    print(arr[s], arr[e], arr[s] + arr[e])
    if arr[s] + arr[e] < x:
        s += 1
    elif arr[s] + arr[e] > x:
        e -= 1
    else:
        answer += 1
        e -= 1

print(answer)