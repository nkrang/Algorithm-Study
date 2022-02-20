import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
sushi = []
for _ in range(N):
    x = int(input())
    sushi.append(x)

result = 0

for i in range(N):
    temp = sushi[i:i+k]
    if i > N-k:
        temp = sushi[i:]
        temp += sushi[:k-N+i]

    temp = set(temp)
    value = len(temp)
    if c not in temp:
        value += 1
    result = max(result, value)
    
    if value == k+1:
        break

print(result)