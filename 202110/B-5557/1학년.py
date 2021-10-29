import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
answer = 0

memo = [[0] * 21 for _ in range(n-1)]

memo[0][numbers[0]] += 1

for i in range(1, n-1):
    for j in range(21):
        if memo[i-1][j] != 0:
            if 0 <= j + numbers[i] <= 20:
                memo[i][j+numbers[i]] += memo[i-1][j] 
            if 0 <= j - numbers[i] <= 20:
                memo[i][j-numbers[i]] += memo[i-1][j]

print(memo[n-2][numbers[-1]])

