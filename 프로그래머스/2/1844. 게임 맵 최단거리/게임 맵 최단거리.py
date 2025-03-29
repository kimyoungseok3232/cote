from collections import deque
def solution(maps):
    n, m = len(maps), len(maps[0])
    st = (0, 0, 1)
    q = deque([st])
    maps[0][0] = 0
    while q:
        x,y,t = q.popleft()
        if x == n-1 and y == m-1: break
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            tx, ty = x+dx, y+dy
            if tx < 0 or tx == n or ty < 0 or ty == m: continue
            if maps[tx][ty] == 1: 
                maps[tx][ty] = 0
                q.append((tx,ty,t+1))
    else: t = -1
    return t