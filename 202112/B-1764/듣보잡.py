import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = dict()
for _ in range(N):
    name = input().strip('\n')
    arr[name] = 0

result = []
for _ in range(M):
    name = input().strip('\n')
    if name in arr:
        result.append(name)

print(len(result))
for x in result:
    print(x)