from itertools import permutations
n, m = map(int, input().split())
for i in permutations(sorted(input().split(), key = lambda x: int(x)), m): 
    print(' '.join(i))