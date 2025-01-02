import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def dfs(x):
    while x in l and l[x]:
        v = l[x].pop()
        l[v].discard(x)
        dfs(v)
    if x in l: del l[x]
n, m = map(int, input().split())
l = {i+1:set() for i in range(n)}
for i in range(m):
    a, b = map(int, input().split())
    l[a].add(b)
    l[b].add(a)
c = 0
while l:
    dfs(list(l.keys())[0])
    c += 1
print(c)