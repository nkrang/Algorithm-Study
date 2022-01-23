import sys
input = sys.stdin.readline

n = int(input())
nums = []
for _ in range(n):
    x = int(input())
    nums.append(x)

maxi = 0
result = []

def dfs(index, value, depth):
    global maxi, result
    if len(index) > maxi:
        if index == value:
            result = value
            maxi = len(index)
    
    if depth == n:
        return

    print(index)
    index.add(depth+1)
    value.add(nums[depth])
    dfs(index, value, depth + 1)
    index.remove(depth+1)
    value.remove(nums[depth])
    print(index)
    dfs(index, value, depth + 1)

dfs(set([]), set([]), 0)

print(maxi)
for x in result:
    print(x)