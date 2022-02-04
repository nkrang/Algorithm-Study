def cal_fee(fees, spent):
    mintime, minfee, pertime, perfee = fees
    if spent <= mintime:
        return minfee
    else:
        temp = (spent - mintime) / pertime
        if temp % 1 != 0:
            temp = int(temp) + 1
        return minfee + int(temp) * perfee

def cal_minute(intime, outtime):
    intime = intime.split(':')
    outtime = outtime.split(':')
    inminute = int(intime[0]) * 60 + int(intime[1])
    outminute = int(outtime[0]) * 60 + int(outtime[1])
    return outminute - inminute


def solution(fees, records):
    answer = []
    incar = dict()
    time = dict()
    car_list = []
    for r in records:
        x, y, m = map(str, r.split())
        if m == 'IN':
            incar[y] = x
            if y not in car_list:
                car_list.append(y)
            if y not in time:
                time[y] = 0
        else:
            time[y] += cal_minute(incar[y], x)
            incar.pop(y)

    for y in incar:
        time[y] += cal_minute(incar[y], "23:59")


    car_list.sort()
    for x in car_list:
        answer.append(cal_fee(fees, time[x]))

    return answer

solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])
