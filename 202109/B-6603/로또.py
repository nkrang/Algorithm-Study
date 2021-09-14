import sys
input = sys.stdin.readline

def dfs(i, res):
    if len(res) == 6:
        for x in res:
            print(x, end= ' ')
        print()
        return
    else:
        if i == pool[0] + 1:
            return
        else:
            res.append(pool[i])
            dfs(i+1, res)
            res.pop()
            dfs(i+1, res)

while True:
    pool = list(map(int, input().split()))
    if pool == [0]:
        break
    else:
        res = []
        dfs(1, res)
        print()


