import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = []
for _ in range(N):
    n, a, b, c = map(int, input().split())
    arr.append((a, b, c, n))

arr.sort(reverse= True)
print(arr)
last = arr[0]
result = [0] * (N+1)
result[arr[0][3]] = 1
cnt = 1
for i in range(1, N):
    if arr[i][0:3] == last[0:3]:
        result[arr[i][3]] = result[last[3]]
        last = arr[i]
    else:
        result[arr[i][3]] = cnt + 1
        last = arr[i]
    
    cnt += 1
print(result)
print(result[K])