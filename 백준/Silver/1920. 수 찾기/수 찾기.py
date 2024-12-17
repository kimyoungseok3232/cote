import sys
print = sys.stdout.write
n, nlist = input(), set(input().split())
m, mlist = input(), input().split()
res = [1 if num in nlist else 0 for num in mlist]
for i in res: print(f'{i}\n')