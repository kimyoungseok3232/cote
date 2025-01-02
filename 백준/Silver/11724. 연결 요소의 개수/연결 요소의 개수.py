import sys
input = sys.stdin.readline
n, m = map(int, input().split())
l = [set() for i in range(n+1)]
v = set(i for i in range(1, n+1))
for i in range(m):
    a, b = map(int, input().split())
    l[a].add(b)
    l[b].add(a)
c = 0
while v:
    nn = [v.pop()]
    while nn:
        x = nn.pop()
        for y in l[x]:
            if y in v:
                v.remove(y)
                nn.append(y)
    c += 1
print(c)