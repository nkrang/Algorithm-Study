import sys
input = sys.stdin.readline

n = int(input())
mem = [(1, 0), (0, 1)]

for _ in range(n):
    num = int(input())
    if len(mem) < num + 2:
        while len(mem) < num + 2:
            next = (mem[-1][0] + mem[-2][0], mem[-1][1] + mem[-2][1])
            mem.append(next)
        else:
            print(mem[num][0], mem[num][1])
    else:
        print(mem[num][0], mem[num][1])

