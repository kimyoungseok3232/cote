def solution(land):
    answer = [0, 0, 0, 0]
    for low in land:
        tmp = [0, 0, 0, 0]
        for idx, val in enumerate(low):
            tmp[idx] = max(answer[idx-1], answer[idx-2], answer[idx-3]) + val
        answer = tmp
    return max(answer)