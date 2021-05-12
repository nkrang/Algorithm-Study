n = int(input())
time = list(map(int, input().split()))

time.sort()
res = 0

for i in range(n+1):
  for j in range(i):
    res += time[j]

print(res)