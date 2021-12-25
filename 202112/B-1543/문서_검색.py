import sys
input = sys.stdin.readline


x = input().strip('\n')
y = input().strip('\n')

stack = []
answer = 0

for i in x:
    stack.append(i)
    if len(stack) >= len(y):
        if ''.join(stack[-len(y):]) == y:
            stack = []
            answer += 1

print(answer)
