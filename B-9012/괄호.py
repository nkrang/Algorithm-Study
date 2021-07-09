n = int(input())

for _ in range(n):
    line = input()
    st = []
    for x in line:
        if x == '(':
            st.append(x)
        else:
            if len(st) == 0:
                print("NO")
                break
            else:
                st.pop()
    else:
        if len(st) == 0:
            print("YES")
        else:
            print("NO")
