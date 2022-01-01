import sys
input = sys.stdin.readline

N = int(input())
answer = 0
for _ in range(N):
    word = list(map(str, input().strip('\n')))

    stack = []
    for x in word:
        if stack and stack[-1] == x:
            stack.pop()
        else:
            stack.append(x)

    if len(stack) == 0:
        answer += 1

print(answer)