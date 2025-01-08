import sys
input = sys.stdin.readline
n, capacity = map(int, input().split())
dp = {0:0}
for _ in range(n):
    w, v = map(int, input().split())
    for weight, value in list(dp.items()):
        nw, nv = weight+w, value+v
        if nw <= capacity:
            if nw in dp and dp[nw] < nv: dp[nw] = nv
            elif nw not in dp: dp[nw] = nv
print(max(dp.values()))