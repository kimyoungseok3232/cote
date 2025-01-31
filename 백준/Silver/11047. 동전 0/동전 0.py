import sys
input = sys.stdin.readline
n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
res = 0
while k:
    res += k//(c:=coin.pop())
    k %= c
print(res)