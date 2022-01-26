import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

answer = numbers[0]
dp = [numbers[0]]
for i in range(1, n):
    if dp[-1] + numbers[i] > numbers[i]:
        dp.append(dp[-1] + numbers[i])
    else:
        dp.append(numbers[i])

    answer = max(answer, dp[-1])

print(answer)