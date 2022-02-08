import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic = dict()
for _ in range(N):
    x = input().strip('\n')
    dic[x] = 1

answer = 0
for _ in range(M):
    x = input().strip('\n')
    if x in dic:
        answer += 1

print(answer)