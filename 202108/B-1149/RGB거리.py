import sys
input = sys.stdin.readline

cost = []
n = int(input())
for _ in range(n):
    house = list(map(int, input().split()))
    cost.append(house)

#내 이전의 것은 이미 색을 고른 경우, 내가 빨강을 고른 경우면 이전에 초록이나 파랑을 고른 경우와 더해주면 된다
for i in range(1, n):
    cost[i][0] = cost[i][0] + min(cost[i-1][1], cost[i-1][2])
    cost[i][1] = cost[i][1] + min(cost[i-1][0], cost[i-1][2])
    cost[i][2] = cost[i][2] + min(cost[i-1][0], cost[i-1][1])

print(min(cost[n-1]))