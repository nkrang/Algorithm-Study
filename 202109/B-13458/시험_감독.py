import sys
import math
input = sys.stdin.readline

n = int(input())
c = list(map(int, input().split()))
a, b = map(int, input().split())

ans = 0
for x in c:
    if x < a:
        ans += 1
    else:
        ans += math.ceil((x-a)/b) + 1
    
print(ans)