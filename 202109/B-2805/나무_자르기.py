import sys
input = sys.stdin.readline

n, goal = map(int, input().split())
tree = list(map(int, input().split()))
tree.sort()

def makeTree(height):
    ans = 0
    for x in tree:
        if x - height > 0:
            ans += x - height
    return ans

def twoFind(left, right):
    while left <= right:
        center = (left + right) // 2
        # print("c", center)
        temp = makeTree(center)
        # print("t", temp)
        if temp >= goal:
            ans = center
            left = center + 1
        else:
            right = center - 1
    return ans

print(twoFind(0, max(tree)))