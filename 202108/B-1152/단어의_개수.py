line = input()

minus = 0
if line[0] == " ":
    minus += 1
if line[-1] == " ":
    minus += 1

space = 0
for x in line:
    if x == " ":
        space += 1

print(space - minus + 1)