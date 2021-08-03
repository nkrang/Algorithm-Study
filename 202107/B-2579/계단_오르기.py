import sys
input = sys.stdin.readline

n = int(input())
st = []
for _ in range(n):
    st.append(int(input()))

dp = [0] * n

for i in range(0, n):
    if i == 0:
        dp[i] = st[i]
    elif i == 1:
        dp[i] = st[i-1] + st[i]
    elif i == 2:
        dp[i] = max(st[i] + st[i-1], st[i] + st[i-2])
    else:
        dp[i] = max(dp[i-2] + st[i], dp[i-3] + st[i-1] + st[i])

print(dp[n-1])