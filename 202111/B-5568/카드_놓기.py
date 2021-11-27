import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
dic = dict()
for _ in range(n):
    x = int(input())
    if x in dic:
        dic[x] += 1
    else:
        dic[x] = 1

answer = 0
def choose(check, result):
    global answer
    if cnt == k:
        answer += 1
        print(check)
        return

    for i in check:
        if check[i] > 0:
            check[i] -= 1
            choose(check, cnt + 1)
            check[i] += 1

choose(dic, 0)
print(answer)