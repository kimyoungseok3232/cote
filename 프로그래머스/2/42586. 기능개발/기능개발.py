def solution(progresses, speeds):
    answer = []
    progresses = progresses[::-1]
    speeds = speeds[::-1]
    while progresses:
        mul = (100-(progresses[-1]))//speeds[-1]
        if (100-(progresses[-1]))%speeds[-1]: mul += 1
        flag = 1
        count = 0
        for idx in range(len(progresses)-1,-1,-1):
            progresses[idx] += speeds[idx] * mul
            if flag and progresses[idx] >= 100:
                progresses.pop()
                speeds.pop()
                count += 1
            else: flag = 0
        answer.append(count)
    return answer