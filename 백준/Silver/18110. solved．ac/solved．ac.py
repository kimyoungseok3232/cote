import sys
ip = sys.stdin.readline
if n:=int(ip()):
    l = sorted([int(ip()) for _ in range(n)])
    if r:=int(0.5+n*0.15): l = l[r:-r]
    print(int(0.5+sum(l)/(len(l))))
else: print(0)