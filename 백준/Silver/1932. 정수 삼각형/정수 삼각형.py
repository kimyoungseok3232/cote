import sys
input = sys.stdin.readline
n = int(input())
l = [int(input())]
for _ in range(n-1):
    t = list(map(int, input().split()))
    t[0] += l[0]
    for i in range(1,len(t)-1):
        t[i] += max(l[i], l[i-1])
    t[-1] += l[-1]
    l = t
print(max(l))