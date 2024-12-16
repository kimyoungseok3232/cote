import sys
input = sys.stdin.readline
print = sys.stdout.write
n = int(input())
p = []
for i in range(n): p.append(tuple(map(int, input().split())))
for i in sorted(p): print(f'{i[0]} {i[1]}\n')