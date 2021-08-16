import sys
input = sys.stdin.readline

n = int(input())
nums = [x for x in range(1, n+1)]

while len(nums) > 1:
    for i in range((len(nums)+1) // 2):
        nums.pop(i)

print(nums[0])