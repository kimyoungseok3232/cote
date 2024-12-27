import sys
ip = sys.stdin.readline
n = int(ip())
l, c, d, s = [], [], {}, 0
mn, mx, md, ct = 4000, -4000, 0, 0
for _ in range(n):
    v = int(ip())
    s+=v
    l.append(v)
    if v < mn: mn = v
    if v > mx: mx = v
    if v not in d: d[v] = 0
    d[v] += 1
    if ct < d[v]: ct, c = d[v], [v]
    elif ct == d[v]: c.append(v)
l.sort(), c.sort()
print(int(s/n+0.5) if s>0 else int(s/n-0.5))
print(l[n//2])
print(c[1] if len(c)>1 else c[0])
print(mx-mn)