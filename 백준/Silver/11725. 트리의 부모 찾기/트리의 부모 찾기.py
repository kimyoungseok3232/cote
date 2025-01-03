import sys
input = sys.stdin.readline
n = int(input())
l = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    l[a].append(b)
    l[b].append(a)
t = [1]
v = {1:0}
p = [0] * (n+1)
while t:
    x = t.pop()
    while l[x]:
        y = l[x].pop()
        if y in v: continue
        p[y] = x
        t.append(y)
        v[y] = 0
print(*p[2:])