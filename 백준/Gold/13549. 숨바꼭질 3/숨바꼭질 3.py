from collections import deque
n, k = map(int, input().split())
v = [2] * 100001
q = deque([(n, 0)])
while q:
    t, c = q.popleft()
    while t < 100001 and v[t]:
        if t == k: break
        v[t] = 0
        for i in [t+1, t-1]:
            if -1 < i < 100001 and v[i] == 2:
                v[i] = 1
                q.append((i, c+1))
        t *= 2
    else: continue
    break
print(c)