import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
sushi = []
for _ in range(N):
    x = int(input())
    sushi.append(x)

check = [0] * (d+1)
check[c] = 1
temp = 1

start, end = 0, k

for x in sushi[start:end]:
    if check[x] == 0:
        temp += 1
    check[x] += 1

result = temp

while start < N:
    check[sushi[start]] -= 1
    if check[sushi[start]] == 0:
        temp -= 1
    if check[sushi[end]] == 0:
        temp += 1
    check[sushi[end]] += 1
    result = max(result, temp)
    if result == k+1:
        break

    start += 1
    end += 1
    if end == N:
        end = 0

print(result)