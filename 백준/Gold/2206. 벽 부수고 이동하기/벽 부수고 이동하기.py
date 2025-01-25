import sys
from collections import deque
input = sys.stdin.readline
def solve():
    n, m = map(int, input().split())
    g = [input() for _ in range(n)]
    v = set()
    q = deque()
    v.add((0,0,0))
    q.append((0,0,1,0))
    while q:
        x, y, dist, break_wall = q.popleft()
        if (x, y) == (n-1, m-1): break
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if g[nx][ny] == '0': 
                    if (nx, ny, break_wall) in v: continue
                    q.append((nx, ny, dist+1, break_wall))
                    v.add((nx, ny, break_wall))
                elif break_wall == 0: 
                    if (nx, ny, 1) in v: continue
                    q.append((nx, ny, dist+1, 1))
                    v.add((nx, ny, 1))
    else: dist = -1
    print(dist)
solve()