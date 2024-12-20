import sys
input = sys.stdin.readline
n = int(input())
t = [tuple(map(int, input().split())) for _ in range(n)]
t.sort(key=lambda x: x[0])
t.sort(key=lambda x: x[1])
lt, c = 0, 0
for i in range(n):
    if lt > t[i][0]: continue
    c += 1
    lt = t[i][1]
print(c)