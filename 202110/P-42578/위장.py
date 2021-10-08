def solution(clothes):
    answer = 1
    d = dict()
    for x in clothes:
        if x[1] in d:
            d[x[1]].append(x[0])
        else:
            d[x[1]] = [x[0]]
    for x in d:
        answer *= (len(d[x])+1)
        
    return answer - 1