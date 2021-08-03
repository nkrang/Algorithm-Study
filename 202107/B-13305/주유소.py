import sys
input = sys.stdin.readline

city = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))

cheap = price[0]
total = 0
for i in range(city - 1):
    if price[i] < cheap:
        cheap = price[i]
    total += road[i] * cheap

print(total)
