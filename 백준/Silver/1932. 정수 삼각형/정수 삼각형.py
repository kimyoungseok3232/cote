import sys
input = sys.stdin.readline
n = int(input())
l = [0] * n
for _ in range(n):
    t = list(map(int, input().split()))
    tl = l.copy()
    for i in range(len(t)):
        if i == 0: tl[i] = l[i] + t[i]
        elif i == len(t)-1: tl[i] = l[i-1] + t[i]
        else: tl[i] = max(l[i], l[i-1]) + t[i]
    l = tl
print(max(l))