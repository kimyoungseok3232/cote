import sys
from collections import Counter as C
ip = sys.stdin.readline
l = sorted([int(ip()) for _ in range(int(ip()))])
f = C(l).most_common(2)
print(int(m+0.5) if (m:=sum(l)/len(l))>0 else int(m-0.5))
print(l[len(l)//2])
print(f[1][0] if len(f)>1 and f[0][1] == f[1][1] else f[0][0])
print(l[-1]-l[0])