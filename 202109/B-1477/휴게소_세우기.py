import sys
input = sys.stdin.readline

n, m, length = map(int, input().split())
arr = list(map(int, input().split()))
arr.append(0)
arr.append(length-1)
arr.sort()

left = 0
right = arr[-1]

answer = 0

while left <= right:
    cnt = 0
    mid = (left+right) // 2
    for i in range(len(arr) - 1):
        if (arr[i+1] - arr[i]) > mid:
            cnt += (arr[i+1] - arr[i] - 1) // mid
    
    if cnt > m:
        left = mid + 1
    else:
        right = mid - 1
        answer = mid

print(answer)