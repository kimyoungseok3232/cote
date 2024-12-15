from math import comb
t = int(input())
for i in range(t):
    n, m = int(input()), int(input())
    print(comb(n+m, m-1))