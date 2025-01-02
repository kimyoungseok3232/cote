import sys
input = sys.stdin.readline
n, m = map(int, input().split())
l = {i+1:set() for i in range(n)}
for i in range(m):
    a, b = map(int, input().split())
    l[a].add(b)
    l[b].add(a)
c = 0
while l:
    for i in l: break
    q = l.pop(i)
    while q:
        x = q.pop()
        if x in l: q |= l.pop(x)
    c += 1
print(c)