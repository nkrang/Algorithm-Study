def solution(info, query):
    answer = []
    
    for x in query:
        cnt = 0
        q = []
        for t in list(map(str,x.split())):
            if t != "and":
                q.append(t)
        for y in info:
            one = list(map(str, y.split()))
            if one[-1] > q[-1]:
                for i in range(4):
                    if one[i] != q[i] and q[i] != "-":
                        break
                else:
                    cnt += 1
        answer.append(cnt)

    return answer

info = list(map(str, input().split()))
query = list(map(str, input().split()))
print(solution(info, query))