from collections import deque

def solution(maps):
    for x in range(len(maps)):
        for y in range(len(maps[x])):
            if maps[x][y] == 'S':
                st = [x,y,0]
                break
    
    visited = [[1 if val == 'X' else 0 for val in line] for line in maps]
    
    dxy = [(1,0), (-1,0), (0,1), (0,-1)]
    q = deque([st])
    while q:
        x, y, t = q.popleft()
        if maps[x][y] == 'L': break
        for dx, dy in dxy:
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]) or visited[nx][ny]:
                continue
            visited[nx][ny] = 1
            q.append((nx,ny,t+1))
    else: return -1
    
    visited = [[1 if val == 'X' else 0 for val in line] for line in maps]

    q = deque([(x,y,t)])
    while q:
        x, y, t = q.popleft()
        if maps[x][y] == 'E': break
        for dx, dy in dxy:
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]) or visited[nx][ny]:
                continue
            visited[nx][ny] = 1
            q.append((nx,ny,t+1))
    else: return -1

    return t