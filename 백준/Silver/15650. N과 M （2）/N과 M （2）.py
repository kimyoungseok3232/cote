from itertools import combinations
n, m = map(int, input().split())
for i in combinations([f'{i+1}' for i in range(n)], m): 
    print(' '.join(i))