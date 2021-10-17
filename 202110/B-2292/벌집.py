import sys
input = sys.stdin.readline

n = int(input())

x = 1
i = 0
while True:
    if n <= x:
        print(i+1)
        break
    else:
        i += 1
        x += 6 * i
        

