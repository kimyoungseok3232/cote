import sys
input = sys.stdin.readline
c, n = int(input()), int(input())
l = {i:set() for i in range(1,c+1)}
for _ in range(n):
    a, b = map(int, input().split())
    l[a].add(b)
    l[b].add(a)
v, n = {1}, l[1].copy()
while n:
    nn = n.pop()
    if nn in v: continue
    else:
        n |= l[nn] 
        v.add(nn)
print(len(v)-1)