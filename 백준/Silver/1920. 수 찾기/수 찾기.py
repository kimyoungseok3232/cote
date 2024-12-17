n, nlist = input(), set(input().split())
m, mlist = input(), input().split()
res = '\n'.join(['1' if num in nlist else '0' for num in mlist])
print(res)