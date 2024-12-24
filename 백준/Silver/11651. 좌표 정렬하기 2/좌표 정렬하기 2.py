import sys
input = sys.stdin.readline
n = int(input())
p = sorted([input() for _ in range(n)], key = lambda x: (int(x.split()[1]), int(x.split()[0])))
print(''.join(p))