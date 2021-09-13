import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
x = int(input())

ans = 0
def dfs(x, data):
    data[x] = -2
    for i in range(n):
        if data[i] == x:
            dfs(i, data)

dfs(x, data)
print(data)
for i in range(n):
    #-2 : 삭제된 노드
    #index가 data에 있으면 자식이 있는 거 = 부모 노드
    if data[i] != -2 and i not in data:
        ans += 1

print(ans)
