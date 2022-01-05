line = list(map(str, input().strip('\n')))
stack = []

answer = 0
temp = 1
for i in range(len(line)):
    if line[i] == '(':
        stack.append(line[i])
        temp *= 2
    elif line[i] == '[':
        stack.append(line[i])
        temp *= 3
    elif line[i] == ')':
        if stack and stack[-1] == '(':
            if line[i-1] == '(':
                answer += temp
        else:
            answer = 0
            break
        temp //= 2
        stack.pop()

    elif line[i] == ']':
        if stack and stack[-1] == '[':
            if line[i-1] == '[':
                answer += temp
        else:
            answer = 0
            break
        temp //= 3
        stack.pop()
            
if stack:
    print(0)
else:
    print(answer)