import sys
input = sys.stdin.readline

n = int(input())
pos = [0] * n
cnt = 0

def check(x):
    for i in range(x):
        if pos[i] == pos[x] or abs(pos[i] - pos[x]) == x - i:
            return False
    return True

def solution(queen):
    global cnt
    if queen == n:
        cnt += 1
        return
    else:
        for i in range(n):
            pos[queen] = i
            if check(queen):
                solution(queen + 1)

solution(0)
print(cnt)
