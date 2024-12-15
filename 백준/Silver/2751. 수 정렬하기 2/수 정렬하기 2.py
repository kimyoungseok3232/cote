import sys
input = sys.stdin.readline
print = sys.stdout.write
n = int(input())
v = set()
for i in range(n): v.add(int(input()))
v = list(v)
v.sort()
for i in v: print(f'{i}\n')