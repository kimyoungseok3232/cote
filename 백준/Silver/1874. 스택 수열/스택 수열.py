import sys
input = sys.stdin.readline
n = int(input())
s = [int(input()) for _ in range(n)]
t = [i for i in range(1,n+1)]
r, a, c = [], [], 0
for i in range(n):
    r.append(t[i])
    a.append('+')
    while r and r[-1] == s[c]:
        r.pop()
        a.append('-')
        c += 1
if r: print('NO')
else: print('\n'.join(a))
