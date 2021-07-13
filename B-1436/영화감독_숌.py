n = int(input())

x = 666
cnt = 0
while True:
    if "666" in str(x):
        cnt += 1
    if cnt == n:
        print(x)
        break
    else:
        x += 1