import sys
input = sys.stdin.readline

n, k = map(int, input().split())

dp = [[[[0 for _ in range(436)] for _ in range(31)] for _ in range(31)] for _ in range(31)]

ans = [0] * 31
def go(i, a, b, p):
    #n개 되면 check
    if i == n:
        if p == k:
            return True
        else:
            return False
    #이미 왔던 곳
    if dp[i][a][b][p]:
        return False
    #검사 유무 체크
    dp[i][a][b][p] = True
    #A 추가하면 p 변화 없음
    ans[i] = 'A'
    if go(i + 1, a + 1, b, p):
        return True
    #B 추가하면 앞에 있는 A 만큼 ++
    ans[i] = 'B'
    if go(i + 1, a, b + 1, p + a):
        return True
    #C 추가하면 앞에 있는 A, B 만큼 ++
    ans[i] = 'C'
    if go(i + 1, a, b, p + a + b):
        return True
    return False

if go(0, 0, 0, 0):
    print(''.join(ans[0:n]))
else:
    print(-1)