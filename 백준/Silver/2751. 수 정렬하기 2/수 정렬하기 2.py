import sys
input = sys.stdin.readline
n = int(input())
v = [input() for _ in range(n)]
print(''.join(sorted(v, key = lambda x: int(x))))