import sys
from collections import Counter as C
ip = sys.stdin.readline
l = sorted([int(ip()) for _ in range(int(ip()))])
f = C(l)
print(int(m+0.5) if (m:=sum(l)/len(l))>0 else int(m-0.5))
print(l[len(l)//2])
print(i[1] if len(i:=[k for k, v in f.items() if v == max(f.values())]) > 1 else i[0])
print(max(l)-min(l))