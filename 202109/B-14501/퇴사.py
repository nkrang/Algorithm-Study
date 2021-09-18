import sys
input = sys.stdin.readline

n = int(input())

ans = [0] * n

for i in range(n):
    day, money = map(int, input().split())
    if (i+day-1) < n:
        if i == 0:
            ans[i+day-1] = money
        else:
            ans[i+day-1] = max(max(ans[0:i])+money, ans[i+day-1])
        

print(max(ans))