import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()

    j = 0
    result = 0
    for i in range(N):
        while j < M:
            if B[j] < A[i]:
                j += 1
            else:
                break
        result += j

    print(result)