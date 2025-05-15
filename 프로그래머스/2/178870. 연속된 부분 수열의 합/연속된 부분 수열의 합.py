def solution(sequence, k):
    answer = []
    st = 0
    s = 0
    for idx, num in enumerate(sequence):
        s += num
        while s > k:
            s -= sequence[st]
            st += 1
        if s == k:
            answer.append((st,idx))

    return min(answer, key=lambda x: x[1]-x[0])