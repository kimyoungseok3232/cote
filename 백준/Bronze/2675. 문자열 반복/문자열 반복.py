def mulst(n, val): return val*n
t = int(input())
for _ in range(t):
    n, st = input().split()
    print(''.join(map(lambda x: mulst(int(n), x), list(st))))
    