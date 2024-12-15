import sys
input = sys.stdin.readline
n = int(input())
v = [0] * 10001
for i in range(n): v[int(input())] += 1
for i in range(1,10001):
    iter = v[i]
    for j in range(iter): print(i)