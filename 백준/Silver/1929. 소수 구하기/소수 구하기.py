m, n = map(int, input().split())
t = [False, False]+[True]*(n-1)
for i in range(2, int(n**(1/2))+1):
    if t[i]:
        for j in range(i*i, n+1, i):
            t[j] = False
print('\n'.join([f'{i}' for i in range(m, n+1) if t[i]]))
