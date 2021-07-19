import sys
input = sys.stdin.readline

n = int(input())
first = int(input())
res = [first]
for i in range(n-1):
    temp = []
    nums = list(map(int, input().split()))
    for j in range(len(nums)):
        if j == 0:
            temp.append(res[0] + nums[0])
        elif j < len(nums)-1:
            temp.append(max(res[j] + nums[j], res[j-1] + nums[j]))
        else:
            temp.append(res[j-1] + nums[j])
    else:
        res = temp

print(max(res))