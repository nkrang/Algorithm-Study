import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    N, M = map(int, input().split())
    answer = 1
    for i in range(M, M-N, -1):
        answer *= i
    for i in range(N, 0, -1):
        answer = answer // i
    print(answer)
