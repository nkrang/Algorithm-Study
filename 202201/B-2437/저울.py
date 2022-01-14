import sys
input = sys.stdin.readline

#추를 오름차순 정렬해서 
#하나씩 더하는데 더한 값이 다음 값보다 같거나 큰 경우에만 더한다
#더한 값이 다음 값보다 작은 경우 그 값부터 그 다음 값까지는 만들 수 없음!

n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

answer = 1
for x in numbers:
    if x <= answer:
        answer += x
    else:
        break

print(answer)
    