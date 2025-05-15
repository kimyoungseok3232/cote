

def solution(queue1, queue2):
    answer = 0
    q1, q2 = sum(queue1), sum(queue2)
    p1, p2 = 0, len(queue1)
    queue = queue1+queue2
    while q1 != q2:
        if p1 == len(queue) or p2 == len(queue)+len(queue): break
        if q1 > q2:
            q1 -= queue[p1]
            q2 += queue[p1]
            p1 += 1
        else:
            q1 += queue[p2%len(queue)]
            q2 -= queue[p2%len(queue)]
            p2 += 1
        answer += 1
    else: return answer
    return -1