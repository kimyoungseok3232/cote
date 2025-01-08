import sys
input = sys.stdin.readline
n, capacity = map(int, input().split())
dp = {0:0}
wvlist = [tuple(map(int, input().split())) for _ in range(n)]
wvlist.sort(reverse=True)
for w, v in wvlist:
    tmp = {}
    for value, weight in dp.items():
        nw, nv = weight+w, value+v
        if dp.get(nv, capacity+1) > nw: tmp[nv] = nw
    dp.update(tmp)
print(max(dp))