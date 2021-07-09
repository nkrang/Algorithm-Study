import sys
input = sys.stdin.readline

n = int(input().strip('\n'))

sample = []
for i in range(n, 0, -1):
    sample.append(i)

res = []
st = []
no = False
for _ in range(n):
    num = int(input().strip('\n'))
    while True:
        if st and st[-1] == num:
            res.append("-")
            st.pop()
            break
        else:
            if not sample:
                no = True
                break
            else:
                res.append("+")
                st.append(sample.pop())

if no:
    print("NO")
else:
    for x in res:
        print(x)