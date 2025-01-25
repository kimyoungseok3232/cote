import sys
from collections import deque
input = sys.stdin.readline
def solve():
    n, m = map(int, input().split())
    g = [list(map(int, input().rstrip())) for _ in range(n)]
    v = [[[0]*2 for _ in range(m)] for _ in range(n)]
    v[0][0][0] = 1
    q = deque()
    q.append((0,0,0))
    dist = -1
    while q:
        x, y, break_wall = q.popleft()
        if (x, y) == (n-1, m-1):
            dist = v[x][y][break_wall]
            break
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if g[nx][ny] == 0 and v[nx][ny][break_wall] == 0: 
                    q.append((nx, ny, break_wall))
                    v[nx][ny][break_wall] = v[x][y][break_wall]+1
                elif g[nx][ny] == 1 and break_wall == 0 and v[nx][ny][1] == 0:
                    q.append((nx, ny, 1))
                    v[nx][ny][1] = v[x][y][0]+1
    print(dist)
solve()