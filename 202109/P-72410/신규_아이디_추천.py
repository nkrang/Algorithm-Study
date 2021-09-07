def solution(new_id):
    answer = ''
    #1
    new_id = list(new_id.lower())
    #2, 3
    temp = []
    flag = False
    for i in range(len(new_id)):
        if new_id[i].isalpha() or new_id[i].isdigit() or new_id[i] in ['-', '_']:
            temp.append(new_id[i])
            flag = False
        elif new_id[i] == "." and flag == False:
            flag = True
            temp.append(new_id[i])
    new_id = temp
    #4
    if new_id:
        if new_id[0] == ".":
            new_id.pop(0)
    if new_id:
        if new_id[-1] == ".":
            new_id.pop()
    #5
    else:
        new_id = ['a']
    #6
    if len(new_id) > 15:
        new_id = new_id[0:15]
    if new_id[-1] == ".":
        new_id.pop()
    #7
    while len(new_id) < 3:
        new_id.append(new_id[-1])

    answer = ''.join(new_id)
    return answer

new_id = input()
print(solution(new_id))