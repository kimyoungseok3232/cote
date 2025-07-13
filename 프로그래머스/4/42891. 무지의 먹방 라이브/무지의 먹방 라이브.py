def solution(food_times, k):
    sorted_list = sorted(food_times)
    val = k//(len(food_times))

    for idx, time in enumerate(sorted_list):
        if val >= time:
            k -= time
            val = k//((len(food_times)-idx-1) or 1)
        else:
            k -= val*(len(food_times)-idx)
            break
    else:
        return -1
    
    food_times = [time-val if time > val else 0 for time in food_times]
    
    for idx, time in enumerate(food_times):
        if time:
            if k:
                k -= 1
            else:
                break
    else:
        for idx, time in enumerate(food_times):
            if time: break
            
    return idx+1