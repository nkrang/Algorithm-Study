from itertools import combinations

def solution(info, query):
    answer = []
    
    info_dict = dict()
    for x in info:
        x = x.split()
        key = x[:-1]
        val = x[-1]
        for i in range(5):
            for y in combinations(key, i):
                info_key = ''.join(y)
                if info_key in info_dict:
                    info_dict[info_key].append(int(val))
                else:
                    info_dict[info_key] = [int(val)]
    
    for k in info_dict:
        info_dict[k].sort()
    
    for q in query:
        q = q.split()
        key = q[:-1]
        val = int(q[-1])
        while "and" in key:
            key.remove("and")
        while "-" in key:
            key.remove("-")
        q_key = ''.join(key)
        cnt = 0
        if q_key in info_dict:
            score = info_dict[q_key]
            left = 0
            right = len(score)-1
            while left <= right:
                mid = (left + right) // 2
                if val > score[mid]:
                    left = mid + 1
                elif val <= score[mid]:
                    right = mid - 1
            answer.append(len(score) - left)
        else:
            answer.append(0)

    return answer