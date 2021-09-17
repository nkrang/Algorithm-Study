from collections import deque

def solution(enter, leave):
    answer = [0] * len(enter)
    meet = [[] for _ in range(len(enter))]
    

    leave = deque(leave)
    temp = enter.index(leave[0])
    room = enter[0:temp]
    room = deque(room)
    print(room)
    for x in room:
        answer[x-1] = len(room)
    answer[leave[0] - 1] = len(room)
    print(answer)

    l = 1
    e = temp
    while l < len(leave):
        print(room)
        print(answer)
        while e < len(enter) and leave[l] not in room:
            room.append(enter[e])
            e += 1
        print(room)
        room.remove(leave[l])
        l += 1

    return answer

print(solution([1, 4, 2, 3], [2, 1, 3, 4]))