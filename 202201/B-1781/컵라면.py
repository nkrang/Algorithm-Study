import sys
input = sys.stdin.readline
import heapq as hq

N = int(input())
arr = []
for _ in range(N):
    x, y = map(int, input().split())
    arr.append((x, y))

#마감일 작은 순으로 정렬
arr.sort()
heap = []

#배열 돌면서
for x, y in arr:
    #힙에 컵라면 수 push
    hq.heappush(heap, y)
    #넣은 후 마감일 체크
    #마감일이 n이면 n개의 숙제를 할 수 있기 때문에 heap의 길이가 n을 넘어가면 안됨
    if len(heap) > x:
        #만약 넘으면 제일 작은 값 pop
        hq.heappop(heap)

print(sum(heap))