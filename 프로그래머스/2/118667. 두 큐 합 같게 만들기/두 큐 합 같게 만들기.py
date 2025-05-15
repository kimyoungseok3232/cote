

def solution(queue1, queue2):
    answer = 0
    diff = sum(queue1) - sum(queue2)
    p1, p2 = 0, 0
    while diff != 0:
        if p1 == len(queue1)+len(queue2) or p2 == len(queue1)+len(queue2): break
        if diff > 0:
            if p1 < len(queue1): val = queue1[p1]
            else: val = queue2[p1%len(queue1)]
            diff -= 2*val
            p1 += 1
        else:
            if p2 < len(queue1): val = queue2[p2]
            else: val = queue1[p2%len(queue2)]
            diff += 2*val
            p2 += 1
        answer += 1
    else: return answer
    return -1