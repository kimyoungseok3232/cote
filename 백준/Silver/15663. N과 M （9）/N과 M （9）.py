import sys
from itertools import permutations
print = sys.stdout.write
n, m = map(int, input().split())
v = set()
for i in permutations(sorted(input().split(), key = int), m): 
    if (st:=' '.join(i)+'\n') in v: continue
    print(st)
    v.add(st)