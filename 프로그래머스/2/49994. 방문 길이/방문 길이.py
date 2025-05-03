def solution(dirs):
    visited = set()
    now = (0,0)
    for di in dirs:
        if di == 'U' and now[1] < 5:
            next = (now[0],now[1]+1)
        elif di == 'D' and now[1] > -5:
            next = (now[0],now[1]-1)
        elif di == 'R' and now[0] < 5:
            next = (now[0]+1,now[1])
        elif di == 'L' and now[0] > -5:
            next = (now[0]-1,now[1])
        else: continue
        visited.add((min(now, next),max(now,next)))
        now = next
    print(visited)
    return len(visited)