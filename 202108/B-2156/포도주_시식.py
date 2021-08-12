import sys
input = sys.stdin.readline

n = int(input())
wine = []
for _ in range(n):
    wine.append(int(input()))

# 경우는 세가지
# 1. 이번 와인을 마시고, 저번 와인도 마신 경우
# 전전 와인을 마시지 않아야함 = 전전전 와인은 마심 => dp[-3](전전전 와인 최대값) + wine[-1](전 와인) + 지금 와인
# 2. 이번 와인을 마시고, 저번 와인은 마시지 않은 경우
# dp[-2](전전 와인의 최대값) + 지금 와인
# 3. 이번 와인을 마시지 않은 경우
# dp[-1](전 와인의 최대값)

# 3번째의 경우 전전전 와인의 최대값을 구할 수 없으므로 0을 넣고 시작
if n > 1: 
    dp = [0, wine[0], wine[0] + wine[1]]
else:
    dp = [0, wine[0]]

for i in range(3, n+1):
    case1 = dp[i-3] + wine[i-2] + wine[i-1]
    case2 = dp[i-2] + wine[i-1]
    case3 = dp[i-1]
    dp.append(max(case1, case2, case3))

print(dp[-1])

