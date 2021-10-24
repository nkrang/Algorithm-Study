import sys
input = sys.stdin.readline

n = int(input())
line = list(map(int, input().split()))
result = []
for i in range(n):
    x = line[i]
    temp = line[0:i]
    res = 0
    for j in range(len(temp) - 1, -1, -1):
        if temp[j] > x:
            res = j + 1
            break
    result.append(res)

for x in result:
    print(x, end=" ")
