import sys
from itertools import permutations
print = sys.stdout.write
n, m = map(int, input().split())
for i in permutations(sorted(input().split(), key = int), m): 
    print(' '.join(i)+'\n')