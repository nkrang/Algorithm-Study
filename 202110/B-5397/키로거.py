import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    stc = input().strip('\n')
    left, right = [], []
    for x in stc:
        if x == '<':
            if left:
                right.append(left.pop())
        elif x == '>':
            if right:
                left.append(right.pop())
        elif x == '-':
            if left:
                left.pop()
        else:
            left.append(x)
        
    for x in range(len(right)):
        left.append(right.pop())
    print(''.join(left))