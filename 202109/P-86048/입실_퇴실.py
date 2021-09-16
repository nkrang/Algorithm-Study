from collections import deque

def solution(enter, leave):
    answer = [0] * len(enter)
    meet = [[] for _ in range(len(enter))]
    room = []
    room = deque(room)

    leave = deque(leave)

    l = 0
    e = 0
    while l < len(leave):
        print(room)
        print(answer)
        while e < len(enter) and leave[l] not in room:
            room.append(enter[e])
            e += 1
        print(room)
        for x in room:
            for y in room:
                if y not in meet[x-1]:
                    meet[x-1].append(y)
        room.remove(leave[l])
        l += 1

    print(meet)
    answer = [len(x)-1 for x in meet]
    return answer

print(solution([1, 4, 2, 3], [2, 1, 3, 4]))