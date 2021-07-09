import sys
input = sys.stdin.readline

n = int(input().strip('\n'))

sample = 1

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
            if sample > n:
                no = True
                break
            else:
                res.append("+")
                st.append(sample)
                sample += 1
if no:
    print("NO")
else:
    for x in res:
        print(x)