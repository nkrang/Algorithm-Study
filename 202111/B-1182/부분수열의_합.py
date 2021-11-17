import sys
input = sys.stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))

check = [0] * N
answer = 0

count = 0

def dfs(total, cnt, plus):
    global answer, count
    count += 1
    if cnt == N:
        if plus != 0 and total == S:
            answer += 1
        return

    dfs(total + nums[cnt], cnt+1, plus+1)
    dfs(total, cnt + 1, plus)


dfs(0, 0, 0)
print(answer)