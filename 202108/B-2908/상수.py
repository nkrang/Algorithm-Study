import sys
input = sys.stdin.readline

num1, num2 = map(int, input().split())
ans1 = 0
ans2 = 0

for _ in range(3):
    ans1 = ans1 * 10 + (num1 % 10)
    num1 = num1 // 10
    ans2 = ans2 * 10 + (num2 % 10)
    num2 = num2 // 10

print(max(ans1, ans2))