import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    stc = input().strip('\n')
    result = []
    p = 0
    for x in stc:
        if x == '<':
            p -= 1
            if p < 0 :
                p = 0
        elif x == '>':
            p += 1
            if p > len(result):
                p = len(result)
        elif x == '-':
            if 0 <= (p-1) < len(result):
                result.pop(p-1)
                p -= 1
        else:
            result.insert(p, x)
            p += 1
        
    print(''.join(result))