import sys
input = sys.stdin.readline
n, m = map(int, input().split())
l = [0]+list(map(int, input().split()))+[0]
for i in range(1,n+1): l[i] += l[i-1]
for i in range(m):
    a, b = map(int, input().split())
    print(l[b]-l[a-1])