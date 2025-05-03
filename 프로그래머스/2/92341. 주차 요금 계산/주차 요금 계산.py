def solution(fees, records):
    in_time = {}
    use_time = {}
    answer = []
    
    for record in records:
        time, car_num, state = record.split()
        time = int(time[:2])*60+int(time[3:])
        if state == 'IN':
            in_time[car_num] = time
        else:
            use_time[car_num] = use_time.get(car_num, 0) + (time-in_time.pop(car_num))
    
    for key in in_time:
        use_time[key] = use_time.get(key, 0) + (23*60+59-in_time[key])
    
    for key in sorted(use_time.keys()):
        fee = fees[1] + (1 + (max(0, (use_time[key] - fees[0]))-1)//fees[2])*fees[3]
        answer.append(fee)
        
    return answer