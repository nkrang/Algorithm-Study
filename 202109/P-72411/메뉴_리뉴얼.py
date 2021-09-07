def solution(orders, course):
    answer = []
    pool = []
    for x in orders:
        pool = list(set(pool) | set(list(x)))
    pool.sort()
    for x in course:
        maxi = 0
        ans = []
        for i in range(0, len(pool)-x+1):
            for j in range(i, len(pool)):
                cnt = 0
                temp = [pool[i], pool[j]]
            for o in orders:
                chk = 0
                for t in temp:
                    if t in list(o):
                        chk += 1
                # print(temp, o, chk)
                if chk == x:
                    cnt += 1
            # print(cnt)
            if cnt > maxi:
                maxi = cnt
                ans = [temp]
            elif cnt == maxi:
                ans.append(temp)
        answer.append(ans)
    return answer


orders = list(map(str, input().split()))
course = list(map(int, input().split()))
print(solution(orders, course))