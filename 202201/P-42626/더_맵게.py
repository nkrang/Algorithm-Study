import heapq as hq

def solution(scoville, K):
    answer = 0

    hq.heapify(scoville)
    while len(scoville) >= 2 and scoville[0] < K:

        x = hq.heappop(scoville)
        y = hq.heappop(scoville)
        temp = x + y * 2
        
        hq.heappush(scoville, temp)
        answer += 1
    
    if scoville and scoville[0] >= K:
        return answer
    else:
        return -1