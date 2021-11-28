import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    if N <= K :
        print(N-1, 'R')
        continue
    left, right = 1, N//K
    jump = 0
    dist = 0

    while left <= right:
        mid = (left + right) // 2
        temp = mid * (mid + 1) * K // 2
        if temp <= N-1:
            jump = mid
            dist = N - 1 - temp
            left = mid+1
        else:
            right = mid-1

    loc = 0
    direction = 0
    result = 0

    if jump % 2 != 0:
        loc = K * (jump // 2 + 1)
        direction = "L"
        result = loc - dist
    else:
        loc = K * (jump // 2) * -1
        direction = "R"
        result = loc + dist

    print(result, direction)

    