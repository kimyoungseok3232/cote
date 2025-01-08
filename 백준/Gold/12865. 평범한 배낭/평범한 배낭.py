import sys
input = sys.stdin.readline
n, capacity = map(int, input().split())
dp = {0:0}
for _ in range(n):
    w, v = map(int, input().split())
    tmp = {}
    for weight, value in dp.items():
        nw, nv = weight+w, value+v
        if nw <= capacity:
            if dp.get(nw, 0) < nv: tmp[nw] = nv
    dp.update(tmp)
print(max(dp.values()))