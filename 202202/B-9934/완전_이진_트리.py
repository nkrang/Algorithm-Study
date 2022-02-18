import sys
input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))

answer = [[] for _ in range(N+1)]

def find_mid(L, R, lvl):
    if L == R:
        answer[lvl].append(seq[L])
        return
    m = (L+R) // 2
    answer[lvl].append(seq[m])
    find_mid(L, m-1, lvl+1)
    find_mid(m+1, R, lvl+1)

find_mid(0, len(seq)-1, 0)

for i in range(N):
    for x in answer[i]:
        print(x, end=' ')
    print()