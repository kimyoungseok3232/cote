def dfs(map, c):
    l, s = len(map), sum(sum(row) for row in map)
    if s == l*l: c[1] += 1
    elif s == 0: c[0] += 1
    else:
        l //= 2
        for i in range(0,2*l,l):
            nmap = [map[j][i:i+l] for j in range(0, l)]
            dfs(nmap, c)
            nmap = [map[j][i:i+l] for j in range(l, 2*l)]
            dfs(nmap, c)
p = [list(map(int,input().split())) for _ in range(int(input()))]
c = [0, 0]
dfs(p, c)
print(c[0])
print(c[1])