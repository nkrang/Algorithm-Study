import math

def solution(progresses, speeds):
    answer = []
    cd = []
    for i in range(len(progresses)):
        day = (100 - progresses[i]) / speeds[i]
        cd.append(math.ceil(day))
    
    answer = [1]
    last = cd[0]
    for i in range(1, len(cd)):
        print(cd[i], last)
        if cd[i] <= last:
            answer[-1] += 1
        else:
            answer.append(1)
            last = cd[i]


    return answer


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))