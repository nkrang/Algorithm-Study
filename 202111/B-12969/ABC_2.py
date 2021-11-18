import sys
input = sys.stdin.readline

n, k = map(int, input().split())

answer = ''
check = [[[0 for _ in range(k+1)] for _ in range(n+1)] for _ in range(n+1)]

def solution(case, a, b, S):
    global answer

    if case > k:
        return

    if len(S) == n:
        if case == k:
            answer = S
        return
    
    if check[a][b][case] != 0:
        return

    check[a][b][case] = 1

    solution(case, a+1, b, S+'A')
    solution(case+a, a, b+1, S+'B')
    solution(case+a+b, a, b, S+'C')

solution(0, 0, 0, '')
if answer == '':
    print(-1)
else:
    print(answer)