line = input().split("-")

for i in range(len(line)):
    plus = line[i].split("+")
    sum = 0
    for x in plus:
        sum += int(x)
    else:
        line[i] = sum

res = line[0]
for i in range(1, len(line)):
    res -= line[i]

print(res)
