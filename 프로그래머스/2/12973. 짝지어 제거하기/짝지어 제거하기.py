def solution(s):
    tmp = [0]
    for i in s:
        if tmp[-1] == i: tmp.pop()
        else: tmp.append(i)
    if len(tmp) == 1: return 1
    return 0