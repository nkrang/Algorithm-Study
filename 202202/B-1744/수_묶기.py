import sys
input = sys.stdin.readline

n = int(input())

plus = []
zero = 0
minus = []
one = 0

for _ in range(n):
    x = int(input())
    if x > 1:
        plus.append(x)
    elif x == 0:
        zero += 1
    elif x == 1:
        one += 1
    else:
        minus.append(x)

answer = 0
temp = 0
for x in sorted(plus, reverse= True):
    if temp == 0:
        temp = x
    else:
        answer += temp * x
        temp = 0
answer += temp

temp = 0
for x in sorted(minus):
    if temp == 0:
        temp = x
    else:
        answer += temp * x
        temp = 0

if zero == 0:
    answer += temp

answer += one

print(answer)
