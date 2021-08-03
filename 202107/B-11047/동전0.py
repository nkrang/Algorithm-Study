n, k = map(int, input().split())
coins = []
cnt = 0

for i in range(n):
  coins.append(int(input()))
    
for i in range(1, n+1):
  cnt += k // coins[n - i]
  k = k % coins[n - i]

print(cnt)