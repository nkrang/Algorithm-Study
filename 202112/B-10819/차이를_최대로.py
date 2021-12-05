import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

c = [0] * N
answer = 0
def dfs(check, total, arr):
    global answer
    if len(arr) == N:
        answer = max(total, answer)
        return
    for i in range(N):
        if check[i] == 0:
            check[i] = 1
            arr.append(numbers[i])
            if len(arr) <= 1:
                dfs(check, total, arr)
            else:
                dfs(check, total + abs(arr[-2] - numbers[i]), arr)
            arr.pop()
            check[i] = 0

dfs(c, 0, [])
print(answer)