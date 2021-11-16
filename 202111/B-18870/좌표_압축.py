import sys
input = sys.stdin.readline

N = int(input())
pos = list(map(int, input().split()))
sortedpos = sorted(pos)

dic = dict()
cnt = 0
for x in sortedpos:
    if x not in dic:
        dic[x] = cnt
        cnt += 1

for x in pos:
    print(dic[x], end=' ')