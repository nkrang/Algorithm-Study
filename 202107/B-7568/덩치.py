n = int(input())

body = []
for _ in range(n):
    w, h = map(int, input().split())
    body.append([w, h])

res = [1] * n

for i in range(n):
    me = body[i]
    for j in range(n):
        you = body[j]
        if you[0] > me[0] and you[1] > me[1]:
            res[i] += 1

for x in res:
    print(x, end=" ")