import sys
input = sys.stdin.readline
k, n = map(int, input().split())
l = [int(input()) for _ in range(k)]
mx, mn = sum(l)//n, 0
while mn <= mx:
    m = (mn+mx)//2
    if sum(i//(m or 1) for i in l) < n: mx = m-1
    else: mn = m+1
print(mx)