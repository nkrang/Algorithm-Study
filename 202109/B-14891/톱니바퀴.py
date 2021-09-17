import sys
input = sys.stdin.readline

wheel = []
for _ in range(4):
    one = str(input().strip('\n'))
    wheel.append(list(one))

n = int(input())

def move(i, d):
    if d == 1:
        wheel[i].insert(0, wheel[i].pop())
    elif d == -1:
        wheel[i].append(wheel[i].pop(0))    

for _ in range(n):
    circul = [2, 2, 2, 2]
    num, direction = map(int, input().split())
    circul[num-1] = direction
    while 2 in circul:
        for i in range(4):
            if i+1 < 4 and circul[i+1] != 2 and circul[i] == 2:
                #돌려
                if wheel[i][2] != wheel[i+1][6]:
                    circul[i] = circul[i+1] * -1
                else:
                    circul[i] = 0
            elif i-1 >= 0 and circul[i-1] != 2 and circul[i] == 2:
                #돌려
                if wheel[i][6] != wheel[i-1][2]:
                    circul[i] = circul[i-1] * -1
                else:
                    circul[i] = 0
    

    for i in range(4):
        move(i, circul[i])
ans = 0
for i in range(4):
    if wheel[i][0] == '1':
        ans += 2 ** i

print(ans)