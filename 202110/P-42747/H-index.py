def solution(citations): 
    citations = sorted(citations)
    n = len(citations)
    h_index = 0 
    for idx, citation in enumerate(citations): 
        if citation >= (n - idx): 
            h_index = (n - idx) 
            break 
    return h_index


print(solution([4, 0, 6, 2, 5]))
print(solution([3, 0, 6, 1, 5]))
print(solution([0, 0, 1]))

#출처
#https://dhsong10.tistory.com/35