from collections import deque
n, k = map(int, input().split())
v = [1] * 100001
vd = [1] * 100001
q = deque([(n, 0)])
while q:
    t, c = q.popleft()
    tmp = t
    while tmp < 100001 and vd[tmp]:
        if tmp == k: break
        v[tmp] = 0
        vd[tmp] = 0
        for i in [tmp+1, tmp-1]:
            if -1 < i < 100001 and v[i]:
                v[i] = 0
                q.append((i, c+1))
        tmp *= 2
    else: continue
    break
print(c)