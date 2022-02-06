import sys
input = sys.stdin.readline

answer = 0
n = int(input())
for x in range(1, n+1):
    arr = list(map(int, str(x)))
    diff = 0
    for i in range(len(arr)-1):
        if i == 0:
            diff = arr[1] - arr[0]
        else:
            if arr[i+1] - arr[i] != diff:
                break
    else:
        answer += 1

print(answer)
        