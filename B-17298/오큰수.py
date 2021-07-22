import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
res = [-1] * n

st = []

for i in range(n):
    while st and (nums[st[-1]] < nums[i]):
        res[st.pop()] = nums[i]
    st.append(i)
        
for x in res:
    print(x, end = " ")

