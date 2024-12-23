import sys
input = sys.stdin.readline
print = sys.stdout.write
n, m = map(int, input().split())
d = {}
for i in range(1,n+1):
    p = input().strip()
    d[p.lower()], d[f'{i}'] = i, p
for i in range(m):
    q = input().strip()
    print(f'{d[q.lower()]}\n')