import sys
input = sys.stdin.readline

n = int(input())

p = [1, 1, 1, 2, 2]
for _ in range(n):
    num = int(input())
    if len(p) >= num :
        print(p[num-1])
    else:
        for i in range(len(p), num):
            p.append(p[i-1] + p[i-5])
        else:
            print(p[num-1])
