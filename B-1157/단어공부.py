
word = input().upper()

#set: 집합 / 중복 제거
alp = list(set(word))
cnt = []

for x in alp:
    cnt.append(word.count(x))

if cnt.count(max(cnt)) >= 2:
    print('?')
else:
    print(alp[cnt.index(max(cnt))])