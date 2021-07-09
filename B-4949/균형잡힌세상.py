import sys
input = sys.stdin.readline

while True:
    line = input().strip('\n')
    if line == '.':
        break
    else:
        st = []
        for x in line:
            if x == '[' or x == '(':
                st.append(x)
            elif x == ']':
                if st and st[-1] == '[':
                    st.pop()
                else:
                    print("no")
                    break
            elif x == ')':
                if st and st[-1] == '(':
                    st.pop()
                else:
                    print("no")
                    break
        else:
            if len(st) == 0:
                print("yes")
            else:
                print("no")