n = int(input())
lost = list(map(int, input().split()))
reserve = list(map(int, input().split()))

def solution(n, lost, reserve):
    # 교집합 제거하는 멋진 코드,,,
    # _reserve = [r for r in reserve if r not in lost]
    # _lost = [l for l in lost if l not in reserve]
    answer = n - len(lost)
    temp = list(set(lost) & set(reserve))
    reserve = list(set(reserve) - set(temp))
    lost = list(set(lost) - set(temp))
    reserve.sort()
    for x in reserve:
        if x-1 in lost:
            lost.remove(x-1)
        elif x+1 in lost:
            lost.remove(x+1)
    answer = n - len(lost)
    return answer

print(solution(n, lost, reserve))