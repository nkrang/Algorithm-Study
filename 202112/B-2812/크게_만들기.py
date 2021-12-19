import sys
input = sys.stdin.readline

from itertools import combinations

N, K = map(int, input().split())
num = list(input().strip('\n'))

combi = list(combinations(num, N-K))
answer = 0
for x in combi:
    temp = int(''.join(x))
    answer = max(answer, temp)

print(answer)