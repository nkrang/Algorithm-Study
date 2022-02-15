import sys
input = sys.stdin.readline

N, x, y = map(int, input().split())

r = 0
while x != y:
    x, y = (x+1)//2, (y+1)//2
    r += 1
print(r)