import sys
input = sys.stdin.readline
print = sys.stdout.write
n = int(input())
p = []
for i in range(n): p.append(list(map(int, input().split())))
p.sort()
for i in p:
    print(f'{i[0]} {i[1]}\n')