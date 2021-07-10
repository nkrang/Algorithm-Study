import sys
input = sys.stdin.readline

n, m = map(int, input.strip().split())
numbers = list(map(int, input().split()))

res = 0
for i in range(n):
    sum1 = numbers[i]
    for j in range(i+1, n):
        sum2 = sum1 + numbers[j]
        for k in range(j+1, n):
            sum3 = sum2 + numbers[k]
            if sum3 <= m and sum3 > res :
                res = sum3

print(res)