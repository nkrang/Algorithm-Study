sn = []
for i in range(1, 10001):
    num = i
    while i > 0:
        num += i % 10
        i = i // 10
    sn.append(num)

sn = set(sn)
sn = list(sn)
sn.sort()

x = 0
for i in range(1, 10001):
    #print("x", sn[x])
    if i < sn[x]:
        print(i)
    elif i == sn[x]:
        x += 1