import sys
input = sys.stdin.readline
n, m = map(int,input().split())
nl = set(input() for _ in range(n))
res = []
for _ in range(m):
    if (i:=input()) in nl: res.append(i)
print(len(res))
print(''.join(sorted(res)))