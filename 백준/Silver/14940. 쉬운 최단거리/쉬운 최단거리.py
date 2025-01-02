n, m = map(int, input().split())
l = [input().split() for _ in range(n)]
for i in range(n):
    for j in range(m): 
        if l[i][j] == '2': break
    else: continue
    break
r = [['-1' if l[i][j] == '1' else '0' for j in range(m)] for i in range(n)]
c, nn = 1, [(i, j)]
while nn:
    tn = []
    while nn:
        x, y = nn.pop()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx > n-1 or ny > m-1: continue
            if r[nx][ny] == '-1' and l[nx][ny] == '1':
                r[nx][ny] = f'{c}'
                tn.append((nx, ny))
  
    nn = tn
    c += 1
for i in r: print(' '.join(i))