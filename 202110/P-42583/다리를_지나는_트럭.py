from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    tn = len(truck_weights)
    complete = 0
    truck_weights = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    total = 0
    while True:
        answer += 1
        t = bridge.popleft()
        if t != 0:
            complete += 1
            total -= t
        if complete == tn:
            break
        #sum 쓰면 시간초과남..!!!
        if truck_weights and total + truck_weights[0] <= weight:
            total += truck_weights[0]
            bridge.append(truck_weights.popleft())
        else:
            bridge.append(0)
    return answer

print(solution(2, 10, [7,4,5,6]))