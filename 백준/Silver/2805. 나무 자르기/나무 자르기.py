n, m = map(int, input().split())
d = {}
for x in map(int, input().split()):
    if x in d: d[x]+=1
    else: d[x]=1
mx = max(d)
mn = max(mx-m, 0)
while mn <= mx:
    mid = (mn + mx) // 2
    if sum(max(0, (i-mid)*d[i]) for i in d) < m: mx = mid - 1
    else: mn = mid + 1
print(mx)