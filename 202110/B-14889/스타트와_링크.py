import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
matrix = []
for _ in range(n):
    line = list(map(int, input().split()))
    matrix.append(line)
    
ans = 20000

def check(team):
    temp = list(combinations(team, 2))
    total = 0
    for x, y in temp:
        total += matrix[x][y]
        total += matrix[y][x]
    return total
    
mem  = [i for i in range(n)]
partition = list(combinations(mem, n//2))

start = 0
link = 0
for x in partition:
    opposite = []
    start = check(x)
    for y in mem:
        if y not in x:
            opposite.append(y)
    link = check(opposite)
    ans = min(ans, abs(start-link))

print(ans)


# def team(i):
#     if i == n :
#         return
#     if t.count(1) == n//2:
#         #실행
#         start = []
#         link = []
#         for j in range(n):
#             if t[j] == 0:

#         return
#     t[i] = 1
#     team(i+1)
#     t[i] = 0
#     team(i+1)