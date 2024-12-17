import sys
from collections import defaultdict
print = sys.stdout.write
n, d = input(), defaultdict(int)
for i in input().split(): d[i] += 1
m = input()
for i in input().split(): print(f'{d[i]}\n')