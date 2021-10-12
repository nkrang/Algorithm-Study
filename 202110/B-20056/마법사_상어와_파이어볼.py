import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
balls = dict()
for _ in range(M):
    x, y, m, s, d = map(int, input().split())
    balls[(x, y)] = [[m, s, d]]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
def move(dic):
    balls = dict()
    for k in dic:
        x, y = k
        for m, s, d in dic[(x, y)]:

            nx = x + dx[d] * s
            ny = y + dy[d] * s

            if nx > N:
                nx = nx % N
            if nx < 1:
                while nx < 1:
                    nx += N
            if ny > N:
                ny = ny % N
            if ny < 1:
                while ny < 1:
                    ny += N

            if (nx, ny) in balls:
                balls[(nx, ny)].append([m, s, d])
            else:
                balls[(nx, ny)] = [[m, s, d]]
    return balls

def cal(dic):
    balls = dict()
    ans = 0
    for k in dic:
        x, y = k
        summ, sums = 0, 0
        chk = 0
        l = len(dic[(x, y)])
        if l == 1:
            balls[(x, y)] = dic[(x, y)]
            ans += dic[(x, y)][0][0]
        else:
            for m, s, d in dic[(x, y)]:
                summ += m
                sums += s
                chk += d % 2
            #방향
            if chk == 0 or chk == l:
                chk = 0
            else:
                chk = 1

            summ = summ // 5
            sums = sums // l
            
            balls[(x, y)] = []
            if summ != 0:
                for i in range(4):
                    balls[(x, y)].append([summ, sums, i * 2 + chk])
            
            ans += summ * 4
       
    return balls, ans

res = 0
for _ in range(K):
    balls = move(balls)
    balls, res = cal(balls)

print(res)
