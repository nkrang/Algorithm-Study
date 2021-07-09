n = int(input())
st = []
for _ in range(n):
    x = int(input())
    if x == 0:
        st.pop()
    else:
        st.append(x)
print(sum(st))