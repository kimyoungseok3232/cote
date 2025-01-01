n, m = map(int, input().split())
l = sorted(map(int, input().split()), reverse=True)
mx = l[0]
mn = max(mx-m, 0)
while mn <= mx:
    mid = (mn + mx) // 2
    if sum(max(i - mid, 0) for i in l) < m: mx = mid - 1
    else: mn = mid + 1
print(mx)