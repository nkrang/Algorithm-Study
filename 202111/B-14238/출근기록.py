import sys
input = sys.stdin.readline

A = list(input().strip('\n'))

def solution(left, result, cnt = 0):
    if cnt == len(A):
        print(''.join(result))
        sys.exit(0)

    for x in left:
        if x == 'A':
            result[cnt] = 'A'
            left.remove('A')
            solution(left, result, cnt+1)
            left.append('A')
        elif x == 'B' and result[cnt-1] != 'B':
            result[cnt] = 'B'
            left.remove('B')
            solution(left, result, cnt+1)
            left.append('B')
        elif x == 'C' and result[cnt-1] != 'C' and result[cnt-2] != 'C':
            result[cnt] = 'C'
            left.remove('C')
            solution(left, result, cnt+1)
            left.append('C')
    else:
        return

solution(A, [0] * len(A))