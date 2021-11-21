import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [x for x in range(n+1)]
dic = dict()
for x in range(n+1):
    dic[x] = [x]

for _ in range(m):
    t, x, y = map(int, input().split())

    if t == 0:
        if x != y and arr[x] != arr[y]:
            temp = dic.pop(arr[y])
            dic[arr[x]] += temp
            for i in temp:
                arr[i] = arr[x]
    else:
        if arr[y] == arr[x]:
            print("YES")
        else:
            print("NO")