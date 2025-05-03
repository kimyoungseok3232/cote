def solution(x, y, n):
    answer = 0
    v = set([y])
    while v:
        tmp = set()
        if x in v: break
        for num in v:
            if num < x: continue
            if num % 3 == 0 : tmp.add(num//3)
            if num % 2 == 0 : tmp.add(num//2)
            tmp.add(num-n)
        v = tmp
        answer+=1
    else: answer = -1
    return answer