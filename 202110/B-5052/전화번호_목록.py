import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    case = int(input())
    phone = []
    for _ in range(case):
        x = str(input().strip('\n'))
        phone.append(x)

    phone.sort()
    #정렬하면 앞 뒤만 비교,,, 키야,,,,,,,,,,
    for i in range(case-1):
        temp = len(phone[i])
        if phone[i] == phone[i+1][0:temp]:
            print("NO")
            break
    else:
        print("YES")